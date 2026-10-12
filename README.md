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
5. [주요 기능](#anchor_features)
6. [구현 화면](#anchor_view)
7. [시작하기](#anchor_start)

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
    <li>영화 예고편 재생</li>
    <li>영화 스틸컷 조회</li>
    <li>장르 / 평점 조회</li>
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
    <li>체크아웃</li>
    <li>토스페이먼츠 결제</li>
  </ul>
</details>
<details>
  <summary>고객센터</summary>
  <ul>
    <li>공지사항</li>
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
</details>
<details>
  <summary>회원가입</summary>
  
  회원가입 기능
  <div><video src="https://github.com/user-attachments/assets/e8f33ce9-e1ea-49fc-9834-6812c7a0d8f8"></video></div>
  
  회원가입 오류
  <div><video src="https://github.com/user-attachments/assets/851081bb-134b-41b9-a97e-c14e4b6d61a9"></video></div>
</details>
<details>
  <summary>로그인</summary>
  
  로그인 기능
  <div><video src="https://github.com/user-attachments/assets/32c8662c-e662-415b-be62-ba012c856006"></video></div>

  로그인 오류
  <div><video src="https://github.com/user-attachments/assets/17d403e5-0971-480d-950d-d9a3e4c45757"></video></div>
</details>
<details>
  <summary>영화 페이지</summary>
  <video src="https://github.com/user-attachments/assets/191fc4e2-af56-44b9-8dcc-fc6463fa7cbf"></video>
</details>
<details>
  <summary>예매</summary>
  <video src="https://github.com/user-attachments/assets/05b9117e-2ef2-4e07-b35c-f658bd2a9479"></video>
</details>
<details>
  <summary>스토어</summary>
  <video src="https://github.com/user-attachments/assets/89dbc589-2979-4721-9763-2830ed043fe3"></video>
</details>
<details>
  <summary>고객센터</summary>

  Q&A
  <div><video src="https://github.com/user-attachments/assets/fbb145bc-0b3d-447f-8846-2ba66d642d3f"></video></div>

  공지사항
  <div><video src="https://github.com/user-attachments/assets/0d8ae8ee-f92a-4eaa-a67c-9c9408f1bc70"></video></div>
</details>
<details>
  <summary>마이페이지</summary>
  
  마이페이지 내역 있음
  <div><video src="https://github.com/user-attachments/assets/e78123be-6e50-46ff-b466-643a87f5c80b"></video></div>

  마이페이지 내역 없음
  <div><video src="https://github.com/user-attachments/assets/a4f8d5e7-c199-41dc-a79f-ae1feff3ea3a"></video></div>
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
