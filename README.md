<div align="center">

# 🎞️ 부귀영화 (BugwuMovie)
<i><small>2026.09.15 ~ 2026.10.07</small></i><br>
Flask로 만든 영화 티켓 예매용 웹사이트

</div>

<br>

## ⫶☰ 목차
1. [프로젝트 소개](#anchor_project)
2. [팀원 소개](#anchor_team)
3. [개발 환경](#anchor_tools)
4. [ERD](#anchor_erd)
5. [폴더구조](#anchor_folder)
6. [주요 기능](#anchor_features)
7. [구현 화면](#anchor_view)
8. [시작하기](#anchor_start)
9. [보고서](#anchor_report)
10. [추가하고 싶은 기능](#anchor_add)

<br>

## <a id="anchor_project"></a>💻 프로젝트 소개
부귀영화는 사용자 가입 및 로그인, 영화 검색, 기존 영화에 대한 "좋아요" 버튼 및 리뷰 기능, 예매 및 결제 시스템, 상품 구매를 위한 스토어, 관리자와의 Q&A 시스템, 예약 확인 또는 취소를 위한 "My Page"와 같은 핵심 기능을 갖춘 영화 예매 웹사이트입니다. 사용자가 원하는 시간과 장소에서 영화 티켓을 예매할 수 있도록, 끊김 없는 경험을 제공하는 것을 목표로 합니다.

<br>

## <a id="anchor_team"></a>👥 팀원 소개

| &nbsp;&nbsp;<img width="150" height="166" alt="3" src="https://github.com/user-attachments/assets/3d393785-126d-4b4e-beb2-5521d0451392" />&nbsp;&nbsp;<br>김유진 | &nbsp;&nbsp;<img width="150" height="166" alt="1" src="https://github.com/user-attachments/assets/99855661-16ed-44e7-a9ff-4dc957a6ea01" />&nbsp;&nbsp;<br>이동형 | &nbsp;&nbsp;<img width="150" height="166" alt="2" src="https://github.com/user-attachments/assets/f28a6521-90de-471c-8923-f8a43c64d900" />&nbsp;&nbsp;<br>조수민 | &nbsp;&nbsp;<img width="150" height="166" alt="4" src="https://github.com/user-attachments/assets/1d5dacca-2714-4525-aa12-1de297b984d3" />&nbsp;&nbsp;<br>함선혜 |
| :---: | :---: | :---: | :---: |
| 팀장 | 그래픽 디자인 | GitHub 관리 | 문서 작업 |
| 메인, 마이페이지,<br>로그인 화면 구현 | 영화 정보,<br>리뷰 페이지 구현 | 내비게이션 바, 영화 목록,<br>예매 페이지 구현 | Q&A 문의 및 답변 구현 |
| 공지사항, 회원탈퇴 구현 | 결제 페이지 구현<br>및 TOSS API 삽입 | 코딩 구조 만들기 | 회원가입 화면 구현 |
| 전체 UI 공통화 작업 | 스토어 페이지 구현 | 명령어 및 스크립트<br>실행 자동화하기 | 시드 데이터 적용 |

<br>

## <a id="anchor_tools"></a>🛠️ 개발 환경
[![개발 환경](https://skillicons.dev/icons?i=html,css,bootstrap,js,flask,py,mysql,figma,docker,github)](https://skillicons.dev)

<br>

## <a id="anchor_erd"></a>📈 ERD
<details>
  <summary>여기를 클릭하여 ERD 보기</summary>
  <img width="7032" height="6136" alt="image" src="https://github.com/user-attachments/assets/eb8c67be-9f7e-45a1-9e19-a48bb3e37164" />
</details>

<br>

## <a id="anchor_folder"></a>🔗 폴더 구조
```
movie/
├── movie/
│   ├── __init__.py         # 앱 팩토리, 블루프린트/필터 등록
│   ├── models.py           # SQLAlchemy 모델
│   ├── filter.py           # Jinja 필터/글로벌 함수
│   ├── views/              # 블루프린트별 라우트
│   │                         (auth, movie, booking, payment, store, mypage, notice, question, answer, fakesite, main)
│   ├── templates/          # Jinja2 템플릿
│   └── static/             # CSS/JS/이미지
├── migrations/             # Flask-Migrate 마이그레이션 스크립트
├── scripts/                # DB 시드 스크립트 (setup.py가 순서대로 실행)
├── config.py               # 앱 설정 (DB URI, SECRET_KEY)
├── setup.py                # 의존성 설치 + 마이그레이션 + 시드 데이터 일괄 실행
├── seed데이터순서.txt       # setup.py 사용법/시드 스크립트 추가 방법 안내
├── .flaskenv               # flask 환경 변수 실행               
└── requirements.txt
```

<br>

## <a id="anchor_features"></a>⚙️ 주요 기능
<details>
  <summary>회원</summary>
  <ul>
    <li>회원가입</li>
    <li>로그인 / 로그아웃</li>
  </ul>
</details>
<details>
  <summary>영화</summary>
  <ul>
    <li>영화 목록 / 상세 조회</li>
    <li>영화 목록 / 제목, 장르 검색</li>
    <li>영화 예고편 재생</li>
    <li>영화 스틸컷 조회</li>
    <li>영화 좋아요</li>
    <li>리뷰 작성</li>
  </ul>
</details>
<details>
  <summary>예매 / 결제</summary>
  <ul>
    <li>극장 · 날짜별 상영정보 조회</li>
    <li>좌석 선택</li>
    <li>BG.POINT 사용</li>
    <li>VIP 쿠폰 / 관람권 / 할인 쿠폰 사용</li>
    <li>토스페이먼츠 V2 샌드박스 결제 연동</li>
  </ul>
</details>
<details>
  <summary>스토어</summary>
  <ul>
    <li>굿즈 / 관람권 / 선물 상품 조회</li>
    <li>장바구니</li>
    <li>토스페이먼츠 결제</li>
  </ul>
</details>
<details>
  <summary>고객센터</summary>
  <ul>
    <li>공지사항 조회 및 검색</li>
    <li>Q&amp;A 문의 작성 및 수정/삭제</li>
    <li>Q&amp;A 답변 작성 및 수정/삭제</li>
  </ul>
</details>
<details>
  <summary>마이페이지</summary>
  <ul>
    <li>예매내역 조회</li>
    <li>구매내역 조회</li>
    <li>취소내역 조회</li>
    <li>예매취소</li>
    <li>제품환불</li>
    <li>회원정보 조회</li>
    <li>회원탈퇴</li>
  </ul>
</details>

<br>

## <a id="anchor_view"></a>👨🏻‍💻 구현 화면
<details>
  <summary>메인 페이지</summary>
  <video src="https://github.com/user-attachments/assets/d7867198-861e-496c-a97b-3145c888c4d5"></video>
  <ul>
    <li>메인 화면에서는 현재 상영 중인 영화 목록을 확인할 수 있다.</li>
    <li>영화 포스터를 클릭하면 해당 영화의 상세 페이지로 이동한다.</li>
  </ul>
  <br>
</details>
<details>
  <summary>회원가입</summary>
  
  회원가입 기능
  <div><video src="https://github.com/user-attachments/assets/e8f33ce9-e1ea-49fc-9834-6812c7a0d8f8"></video></div>
  <ul>
    <li>회원가입 페이지에서 아이디, 비밀번호, 이름, 이메일, 연락처 등 필수 정보를 입력한다.</li>
    <li>새로운 계정을 성공적으로 생성할 수 있다.</li>
  </ul>
  <br>
  회원가입 오류
  <div><video src="https://github.com/user-attachments/assets/851081bb-134b-41b9-a97e-c14e4b6d61a9"></video></div>
  <ul>
    <li>필수 입력 항목이 누락되거나 중복된 아이디를 입력할 경우 유효성 검사 에러 메시지가 출력된다.</li>
    <li>비밀번호 형식 불일치 시 안내 문구가 표시되어 올바른 가입을 유도한다.</li>
  </ul>
  <br>
</details>
<details>
  <summary>로그인</summary>
  
  로그인 기능
  <div><video src="https://github.com/user-attachments/assets/32c8662c-e662-415b-be62-ba012c856006"></video></div>
  <ul>
    <li>상단 메뉴에서 로그인 버튼을 클릭하여 로그인 화면으로 이동한다.</li>
    <li>가입한 계정의 아이디와 비밀번호를 입력하여 서비스에 로그인할 수 있다.</li>
    <li>로그인 성공 시 사용자 맞춤형 상단 메뉴(마이페이지, 예매 내역 등)가 활성화된다.</li>
  </ul>
  <br>
  로그인 오류
  <div><video src="https://github.com/user-attachments/assets/17d403e5-0971-480d-950d-d9a3e4c45757"></video></div>
  <ul>
    <li>존재하지 않는 아이디를 입력하거나 잘못된 비밀번호를 입력할 경우 로그인 실패 알림이 뜬다.</li>
    <li>입력 정보 오류에 대한 적절한 피드백 메시지를 제공하여 재시도를 돕는다.</li>
    <li>로그인 성공 시 사용자 맞춤형 상단 메뉴(마이페이지, 예매 내역 등)가 활성화된다.</li>
  </ul>
  <br>
</details>
<details>
  <summary>영화 페이지</summary>
  <video src="https://github.com/user-attachments/assets/191fc4e2-af56-44b9-8dcc-fc6463fa7cbf"></video>
  <ul>
    <li>전체 영화 목록을 조회할 수 있고 제목 및 장르 카테고리별로 검색하여 볼 수 있다.</li>
    <li>개별 영화 상세 페이지에서는 줄거리, 감독, 배우, 관람가, 평점 등의 상세 정보를 확인할 수 있고 좋아요, 관람평 등을 남길 수 있다.</li>
  </ul>
  <br>
</details>
<details>
  <summary>예매</summary>
  <video src="https://github.com/user-attachments/assets/05b9117e-2ef2-4e07-b35c-f658bd2a9479"></video>
  <ul>
    <li>원하는 영화, 상영 극장, 날짜, 시간대를 단계별로 선택할 수 있다.</li>
    <li>극장 좌석 배치도에서 원하는 좌석을 직접 선택하고 예매 결제 단계로 진행할 수 있다.</li>
    <li>결제 시 BG.POINT / VIP 쿠폰 / 할인 쿠폰을 사용하여 할인을 받을 수 있다.</li>
  </ul>
  <br>
</details>
<details>
  <summary>스토어</summary>
  <video src="https://github.com/user-attachments/assets/89dbc589-2979-4721-9763-2830ed043fe3"></video>
  <ul>
    <li>팝콘, 음료, 콤보 세트 및 영화 관람권 등 다양한 상품을 조회할 수 있다.</li>
    <li>상품 상세 정보 확인 후 장바구니 담기 및 구매(결제) 프로세스를 진행할 수 있다.</li>
  </ul>
  <br>
</details>
<details>
  <summary>고객센터</summary>

  Q&A
  <div><video src="https://github.com/user-attachments/assets/fbb145bc-0b3d-447f-8846-2ba66d642d3f"></video></div>
  <ul>
    <li>문의 게시판에 문의 글들을 조회할 수 있다.</li>
    <li>사용자가 직접 문의 글을 작성하고, 답변을 확인할 수 있다.</li>
  </ul>
  <br>
  공지사항
  <div><video src="https://github.com/user-attachments/assets/0d8ae8ee-f92a-4eaa-a67c-9c9408f1bc70"></video></div>
  <ul>
    <li>영화관 관련 중요 안내 사항, 시스템 점검, 이벤트 소식 등을 최신순으로 확인하고 검색하여 볼 수 있다.</li>
    <li>특정 공지사항을 클릭하여 상세 내용을 조회할 수 있다.</li>
  </ul>
  <br>
</details>
<details>
  <summary>마이페이지</summary>
  <video src="https://github.com/user-attachments/assets/e78123be-6e50-46ff-b466-643a87f5c80b"></video>
  <ul>
    <li>개인 회원 정보(비밀번호, 연락처 등)를 조회하고 수정할 수 있다.</li>
    <li>예매 내역, 스토어 구매 내역 등 개인 활동 기록을 한눈에 관리할 수 있다.</li>
    <li>예매 취소, 구매 취소, 회원 탈퇴를 할 수 있다.</li>
  </ul>
  <br>
</details>

<br>

## <a id="anchor_start"></a>🚀 시작하기
```
git clone https://github.com/moviemoviee/movie.git
cd movie

python -m venv .venv
./venv/Scripts/activate

python setup.py
flask run
```
<br>

## <a id="anchor_report"></a>📑 보고서
[부귀영화.pdf](https://github.com/user-attachments/files/33319327/default.pdf)
<br><br>

## <a id="anchor_add"></a>⚙ 추가하고 싶은 기능
- 모바일 티켓과 입장용 QR코드 생성
- 소셜 간편 로그인(카카오톡, 네이버, 구글 계정 연동으로 1초 만에 회원가입 및 로그인)
- 사용자 문의글(QnA)에 관리자가 직접 답변을 등록하고, 처리 상태를 '답변 완료'로 업데이트하는 기능
- 관심 등록한 영화의 상영 스케줄이 오픈되거나 개봉일이 되었을 때 마이페이지 알림으로 안내
- 회원가입 없이 휴대폰 번호와 비밀번호 입력만으로 예매 진행 및 조회
<br><br>
