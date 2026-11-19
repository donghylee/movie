from datetime import datetime

from movie import db, create_app
from movie.models import Trailer

app = create_app()

trailers = [
    # 인턴
    Trailer(
        movie_id=1,
        title='1차 예고편',
        image_url='/static/img/movie1/1.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24751_301_1.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=1,
        title='2차 예고편',
        image_url='/static/img/movie1/2.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24751_301_2.mp4',
        created_at=datetime.now()
    ),

    # 부활남
    Trailer(
        movie_id=2,
        title='티저 예고편',
        image_url='/static/img/movie2/1.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24724_301_1.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=2,
        title='Comming Soon 영상',
        image_url='/static/img/movie2/2.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24724_301_2.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=2,
        title='메인 예고편',
        image_url='/static/img/movie2/3.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24724_301_3.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=2,
        title='빨간맛 케미 캐릭터 영상',
        image_url='/static/img/movie2/4.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24724_301_4.mp4',
        created_at=datetime.now()
    ),

    # 암살자
    Trailer(
        movie_id=3,
        title='티저 예고편',
        image_url='/static/img/movie3/1.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24623_301_1.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=3,
        title='메인 예고편',
        image_url='/static/img/movie3/2.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24623_301_2.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=3,
        title='메이킹 필름',
        image_url='/static/img/movie3/3.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24623_301_3.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=3,
        title='추적자(들) 예고편',
        image_url='/static/img/movie3/4.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24623_301_4.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=3,
        title='리뷰 예고편',
        image_url='/static/img/movie3/5.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24623_301_5.mp4',
        created_at=datetime.now()
    ),

    # 타짜
    Trailer(
        movie_id=4,
        title='라이벌 예고편',
        image_url='/static/img/movie4/1.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24654_301_1.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=4,
        title='제작기 영상',
        image_url='/static/img/movie4/2.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24654_301_2.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=4,
        title='메인 예고편',
        image_url='/static/img/movie4/3.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24654_301_3.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=4,
        title='20주년 피날레 축전영상',
        image_url='/static/img/movie4/4.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24654_301_4.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=4,
        title='국립 MV 영상',
        image_url='/static/img/movie4/5.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24654_301_5.mp4',
        created_at=datetime.now()
    ),

    # 옵세션
    Trailer(
        movie_id=6,
        title='니키니키니키니키 예고편',
        image_url='/static/img/movie6/1.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24868_301_1.mp4',
        created_at=datetime.now()
    ),

    # 어벤져스
    Trailer(
        movie_id=7,
        title='리어셈블 예고편',
        image_url='/static/img/movie7/1.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24982_301_1.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=7,
        title='인피니티 비전 예고편',
        image_url='/static/img/movie7/2.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24982_301_2.mp4',
        created_at=datetime.now()
    ),

    # 가능한 사랑
    Trailer(
        movie_id=8,
        title='1차 예고편',
        image_url='/static/img/movie8/1.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24725_301_1.mp4',
        created_at=datetime.now()
    ),

    # 레지던트 이블
    Trailer(
        movie_id=9,
        title='티저 예고편',
        image_url='/static/img/movie9/1.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24466_301_1.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=9,
        title='메인 예고편',
        image_url='/static/img/movie9/2.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24466_301_2.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=9,
        title='점프 스트리트 클립',
        image_url='/static/img/movie9/3.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24466_301_3.mp4',
        created_at=datetime.now()
    ),

    # 아버지의 집밥
    Trailer(
        movie_id=10,
        title='예고편',
        image_url='/static/img/movie10/1.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24872_301_1.mp4',
        created_at=datetime.now()
    ),

    # 스파이더맨
    Trailer(
        movie_id=11,
        title='티저 예고편',
        image_url='/static/img/movie11/1.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202607/24329_301_1.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=11,
        title='브랜드 뉴 데이 영상',
        image_url='/static/img/movie11/2.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202607/24329_301_2.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=11,
        title='30초 예고편',
        image_url='/static/img/movie11/3.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202607/24329_301_3.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=11,
        title='메인 예고편',
        image_url='/static/img/movie11/4.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202607/24329_301_4.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=11,
        title='파이널 예고편',
        image_url='/static/img/movie11/5.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202607/24329_301_5.mp4',
        created_at=datetime.now()
    ),

    # 치이카와
    Trailer(
        movie_id=12,
        title='티저 예고편',
        image_url='/static/img/movie12/1.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24708_301_1.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=12,
        title='메인 예고편',
        image_url='/static/img/movie12/2.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24708_301_2.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=12,
        title='더빙 예고편',
        image_url='/static/img/movie12/3.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24708_301_3.mp4',
        created_at=datetime.now()
    ),

    # 알파
    Trailer(
        movie_id=13,
        title='티저 예고편',
        image_url='/static/img/movie13/1.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24933_301_1.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=13,
        title='티저 예고편',
        image_url='/static/img/movie13/2.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24933_301_2.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=13,
        title='티저 예고편',
        image_url='/static/img/movie13/3.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24933_301_3.mp4',
        created_at=datetime.now()
    ),

    # 트루먼의 사랑
    Trailer(
        movie_id=14,
        title='30초 예고편',
        image_url='/static/img/movie14/1.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202608/24698_301_1.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=14,
        title='메인 예고편',
        image_url='/static/img/movie14/2.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202608/24698_301_2.mp4',
        created_at=datetime.now()
    ),

    # 수련
    Trailer(
        movie_id=15,
        title='메인 예고편',
        image_url='/static/img/movie15/1.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24708_301_1.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=15,
        title='30초 예고편',
        image_url='/static/img/movie15/2.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24708_301_1.mp4',
        created_at=datetime.now()
    ),

    # 담요를 입은 사람
    Trailer(
        movie_id=16,
        title='메인 예고편',
        image_url='/static/img/movie16/1.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24833_301_1.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=16,
        title='30초 예고편',
        image_url='/static/img/movie16/2.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24833_301_2.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=16,
        title='추천 영상',
        image_url='/static/img/movie16/3.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24833_301_3.mp4',
        created_at=datetime.now()
    ),

    # 퓨리어스
    Trailer(
        movie_id=17,
        title='메인 예고편',
        image_url='/static/img/movie17/1.jpg',
        trailer_url='https://www.youtube.com/watch?v=wfmNeiSFiHU',
        created_at=datetime.now()
    ),

    # 퍼펙트 슛
    Trailer(
        movie_id=18,
        title='티저 예고편',
        image_url='/static/img/movie18/1.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24937_301_1.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=18,
        title='메인 예고편',
        image_url='/static/img/movie18/2.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24937_301_2.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=18,
        title='30초 예고편',
        image_url='/static/img/movie18/3.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24937_301_3.mp4',
        created_at=datetime.now()
    ),

    # 철들 무렵
    Trailer(
        movie_id=19,
        title='티저 예고편',
        image_url='/static/img/movie19/1.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24757_301_1.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=19,
        title='메인 예고편',
        image_url='/static/img/movie19/1.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24757_301_2.mp4',
        created_at=datetime.now()
    ),

    # 드로스테 저편의 우리들
    Trailer(
        movie_id=20,
        title='티저 예고편',
        image_url='/static/img/movie20/1.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202608/24702_301_1.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=20,
        title='메인 예고편',
        image_url='/static/img/movie20/2.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202608/24702_301_2.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=20,
        title='30초 예고편',
        image_url='/static/img/movie20/3.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202608/24702_301_3.mp4',
        created_at=datetime.now()
    ),

    # 사진의 얼굴
    Trailer(
        movie_id=21,
        title='티저 예고편',
        image_url='/static/img/movie21/1.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24737_301_1.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=21,
        title='티저 예고편',
        image_url='/static/img/movie21/2.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24737_301_2.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=21,
        title='티저 예고편',
        image_url='/static/img/movie21/3.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24737_301_3.mp4',
        created_at=datetime.now()
    ),

    # 빈집의 연인들
    Trailer(
        movie_id=22,
        title='1차 예고편',
        image_url='/static/img/movie22/1.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202608/24675_301_1.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=22,
        title='2차 예고편',
        image_url='/static/img/movie22/2.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202608/24675_301_2.mp4',
        created_at=datetime.now()
    ),

    # 지난 여름
    # Trailer(
    #     movie_id=23,
    #     title='티저 예고편',
    #     image_url='/static/img/movie23/1.jpg',
    #     trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24708_301_1.mp4',
    #     created_at=datetime.now()
    # ),

    # 싱 어게인
    Trailer(
        movie_id=24,
        title='런칭 예고편',
        image_url='/static/img/movie24/1.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24745_301_1.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=24,
        title='오프닝 예고편',
        image_url='/static/img/movie24/2.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24745_301_2.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=24,
        title='메인 예고편',
        image_url='/static/img/movie24/3.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24745_301_3.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=24,
        title="'How to Write a Song(Without You)' 뮤직비디오",
        image_url='/static/img/movie24/4.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24745_301_4.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=24,
        title='파이널 예고편',
        image_url='/static/img/movie24/5.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24745_301_5.mp4',
        created_at=datetime.now()
    ),

    # 어떻게 해야 했을까?
    Trailer(
        movie_id=25,
        title='티저 예고편',
        image_url='/static/img/movie25/1.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202607/24625_301_1.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=25,
        title='메인 예고편',
        image_url='/static/img/movie25/2.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202607/24625_301_2.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=25,
        title='30초 예고편',
        image_url='/static/img/movie25/3.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202607/24625_301_3.mp4',
        created_at=datetime.now()
    ),

    # 델마
    Trailer(
        movie_id=26,
        title='재개봉 30초 예고편',
        image_url='/static/img/movie26/1.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/201808/13136_301_1.mp4',
        created_at=datetime.now()
    ),

    # 캐리어를 끄는 소녀
    Trailer(
        movie_id=27,
        title='티저 예고편',
        image_url='/static/img/movie27/1.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24748_301_1.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=27,
        title='티저 예고편',
        image_url='/static/img/movie27/2.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24748_301_2.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=27,
        title='티저 예고편',
        image_url='/static/img/movie27/3.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202609/24748_301_3.mp4',
        created_at=datetime.now()
    ),

    # 파리의 사생활
    Trailer(
        movie_id=28,
        title='티저 예고편',
        image_url='/static/img/movie28/1.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202607/24465_301_1.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=28,
        title='메인 예고편',
        image_url='/static/img/movie28/2.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202607/24465_301_2.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=28,
        title='30초 예고편',
        image_url='/static/img/movie28/3.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202607/24465_301_3.mp4',
        created_at=datetime.now()
    ),

    # 산양들
    Trailer(
        movie_id=29,
        title='메인 예고편',
        image_url='/static/img/movie29/1.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202607/24581_301_1.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=29,
        title='30초 예고편',
        image_url='/static/img/movie29/2.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202607/24581_301_2.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=29,
        title='스페셜 비하인드 영상',
        image_url='/static/img/movie29/3.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202607/24581_301_3.mp4',
        created_at=datetime.now()
    ),
    Trailer(
        movie_id=29,
        title='추천 영상',
        image_url='/static/img/movie29/4.jpg',
        trailer_url='https://cf.lottecinema.co.kr//Media/MovieFile/MovieMedia/202607/24581_301_4.mp4',
        created_at=datetime.now()
    ),
]
with app.app_context():
    # 이번 리스트에 들어 있는 영화들의 기존 트레일러만 지움 (다른 영화 데이터는 안 건드림)
    movie_ids = {t.movie_id for t in trailers}
    deleted = Trailer.query.filter(
        Trailer.movie_id.in_(movie_ids)
    ).delete(synchronize_session=False)

    db.session.add_all(trailers)
    db.session.commit()

print(f'기존 {deleted}개 삭제, {len(trailers)}개 새로 입력 완료!')