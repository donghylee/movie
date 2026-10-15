// movie_detail.js : 영화 상세 페이지 전용 스크립트
// (템플릿의 {% block script %} 안에서 불러오므로 DOM이 모두 그려진 뒤에 실행됩니다)

// ----- 탭 전환 -----
document.querySelectorAll('.tab-btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
        document.querySelectorAll('.tab-btn').forEach(function (b) { b.classList.remove('active'); });
        btn.classList.add('active');
        document.querySelectorAll('.tab-panel').forEach(function (p) { p.style.display = 'none'; });
        document.getElementById('tab-' + btn.dataset.tab).style.display = 'block';
    });
});

// ----- 예고편 팝업 (HTML의 onclick="openTrailer(...)" 에서 호출하므로 전역 함수로 둬야 함) -----
function openTrailer(url) {
    window.open(
        url,
        'trailerWindow',
        'width=1000,height=600,resizable=yes,scrollbars=yes'
    );
}

var mainTrailerBtn = document.getElementById('mainTrailerBtn');
if (mainTrailerBtn) {
    mainTrailerBtn.addEventListener('click', function () {
        openTrailer(mainTrailerBtn.dataset.trailerUrl);
    });
}

// ----- 관람평 작성 후 돌아왔을 때 관람평 탭 자동 열기 -----
if (window.location.hash === '#tab-review') {
    document.querySelector('.tab-btn[data-tab="review"]').click();
}

// ----- 관람평 페이지네이션 -----
var REVIEWS_PER_PAGE = 4;
var reviewList = document.querySelector('.review-list');
var reviewPagination = document.getElementById('reviewPagination');

if (reviewList && reviewPagination) {
    var reviewItems = reviewList.querySelectorAll('.review-item');
    var reviewPageCount = Math.ceil(reviewItems.length / REVIEWS_PER_PAGE);

    function showReviewPage(page) {
        reviewItems.forEach(function (item, index) {
            var itemPage = Math.floor(index / REVIEWS_PER_PAGE) + 1;
            item.classList.toggle('review-hidden', itemPage !== page);
        });
        reviewPagination.querySelectorAll('.review-page-btn').forEach(function (btn) {
            btn.classList.toggle('active', Number(btn.dataset.page) === page);
        });
    }

    if (reviewPageCount > 1) {
        for (var i = 1; i <= reviewPageCount; i++) {
            var pageBtn = document.createElement('button');
            pageBtn.type = 'button';
            pageBtn.className = 'review-page-btn';
            pageBtn.textContent = i;
            pageBtn.dataset.page = i;
            reviewPagination.appendChild(pageBtn);
        }

        reviewPagination.addEventListener('click', function (e) {
            if (e.target.classList.contains('review-page-btn')) {
                showReviewPage(Number(e.target.dataset.page));
            }
        });
    }

    showReviewPage(1);
}

// ----- 트레일러 슬라이더 -----
const trailerTrack = document.querySelector('.trailer-track');
const trailerItems = document.querySelectorAll('.trailer-item');
const trailerPrev = document.getElementById('trailer-prev');
const trailerNext = document.getElementById('trailer-next');
let trailerIndex = 0;

if (trailerTrack && trailerItems.length > 3) {
    function moveTrailer() {
        const itemWidth = trailerItems[0].offsetWidth + 16;
        trailerTrack.style.transform = `translateX(-${trailerIndex * itemWidth}px)`;
    }

    trailerNext.addEventListener('click', function () {
        trailerIndex++;
        if (trailerIndex > trailerItems.length - 3) {
            trailerIndex = 0;
        }
        moveTrailer();
    });

    trailerPrev.addEventListener('click', function () {
        trailerIndex--;
        if (trailerIndex < 0) {
            trailerIndex = trailerItems.length - 3;
        }
        moveTrailer();
    });

    window.addEventListener('resize', moveTrailer);
}

// ----- 스틸컷 더보기 -----
var stillMoreBtn = document.getElementById('stillMoreBtn');
if (stillMoreBtn) {
    stillMoreBtn.addEventListener('click', function () {
        document.querySelectorAll('#stillGallery .still-hidden').forEach(function (img) {
            img.classList.remove('still-hidden');
        });
        stillMoreBtn.style.display = 'none';
    });
}

// ----- 스틸컷 원본 보기 -----
var stillGallery = document.getElementById('stillGallery');
var stillLightbox = document.getElementById('stillLightbox');
var stillLightboxImg = document.getElementById('stillLightboxImg');

if (stillGallery && stillLightbox) {
    stillGallery.addEventListener('click', function (e) {
        if (e.target.tagName === 'IMG') {
            stillLightboxImg.src = e.target.src;
            stillLightbox.classList.add('show');
        }
    });

    stillLightbox.addEventListener('click', function (e) {
        if (e.target === stillLightbox) {
            stillLightbox.classList.remove('show');
            stillLightboxImg.src = '';
        }
    });
}

// ----- 좋아요 (서버에 저장) -----
var likeTag = document.getElementById('likeTag');
if (likeTag) {
    if (likeTag.dataset.isUser == "true") {
        likeTag.addEventListener('click', function () {
            fetch('/movie/' + likeTag.dataset.movieId + '/like', {
                method: 'POST',
                headers: { 'X-CSRFToken': document.querySelector('meta[name="csrf-token"]').content },
            })
                .then(function (res) { return res.json(); })
                .then(function (data) {
                    likeTag.classList.add('flash');
                    setTimeout(function () {
                        likeTag.classList.remove('flash');
                    }, 250);
                    if (likeTag.classList.contains('liked')) {
                        likeTag.classList.remove('liked');
                        likeTag.innerHTML = `♡ <span id="likeCount">${data.like_count}</span>`;
                    }
                    else {
                        likeTag.classList.add('liked');
                        likeTag.innerHTML = `♥ <span id="likeCount">${data.like_count}</span>`;
                    }
                })
                .catch(function (err) {
                    console.error('좋아요 요청 실패:', err);
                });
        });
    }
}

// ----- 링크 복사 -----
var copyLinkBtn = document.getElementById('copyLinkBtn');
var copyToast = document.getElementById('copyToast');

if (copyLinkBtn) {
    copyLinkBtn.addEventListener('click', function () {
        var url = window.location.href;

        if (navigator.clipboard && navigator.clipboard.writeText) {
            navigator.clipboard.writeText(url).then(showToast).catch(fallbackCopy);
        } else {
            fallbackCopy();
        }

        function fallbackCopy() {
            var temp = document.createElement('textarea');
            temp.value = url;
            temp.style.position = 'fixed';
            temp.style.opacity = '0';
            document.body.appendChild(temp);
            temp.select();
            document.execCommand('copy');
            document.body.removeChild(temp);
            showToast();
        }

        function showToast() {
            copyToast.classList.add('show');
            setTimeout(function () {
                copyToast.classList.remove('show');
            }, 1800);
        }
    });
}
