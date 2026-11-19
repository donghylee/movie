# 베이스 이미지 선택
FROM python:3.12-slim

# 시간대 설정 (KST) + 파이썬 실행 옵션
ENV TZ=Asia/Seoul \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    MALLOC_ARENA_MAX=2

RUN apt-get update && apt-get install -y --no-install-recommends tzdata && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# 작업 디렉토리 생성 및 이동
WORKDIR /app

# 종속성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 전체 프로젝트 복사
COPY . .

# Flask 환경변수 설정
ENV FLASK_APP=movie:create_app

EXPOSE 10000

# 앱 실행
CMD gunicorn -w 1 --threads 4 --timeout 120 -b 0.0.0.0:${PORT:-10000} "movie:create_app()"