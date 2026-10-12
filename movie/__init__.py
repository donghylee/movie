from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

import config

naming_convention = {
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(column_0_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s',
}

db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()

# 애플리케이션 팩토리
def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM 초기 설정
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite'):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)
    from . import models

    # 블루프린트 등록
    from .views import main_views, auth_views, movie_views, question_views, notice_views, answer_views, booking_views, mypage_views, payment_views, fakesite_views, store_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(movie_views.bp)
    app.register_blueprint(notice_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(booking_views.bp)
    app.register_blueprint(mypage_views.bp)
    app.register_blueprint(payment_views.bp)
    app.register_blueprint(fakesite_views.bp)
    app.register_blueprint(store_views.bp)

    # 필터 등록
    from .filter import format_datetime, korean_days
    app.jinja_env.filters['datetime'] = format_datetime
    app.jinja_env.globals['korean_days'] = korean_days

    # 네비바 장바구니 배지용 컨텍스트 프로세서
    @app.context_processor
    def inject_cart_count():
        from flask import g, session
        if not g.get('user'):
            return {'cart_count': 0}
        cart = session.get('cart', [])
        return {'cart_count': sum(item['qty'] for item in cart)}

    # 요청별 메모리 사용량 로그 (원인 찾은 뒤 삭제)
    try:
        import resource
    except ImportError:  # Windows(PyCharm 로컬 실행)에서는 건너뜀
        resource = None

    if resource:
        from flask import request

        @app.after_request
        def log_memory(response):
            peak_mb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
            app.logger.warning(f"[MEM] {request.method} {request.path} -> peak {peak_mb:.0f}MB")
            return response

    return app