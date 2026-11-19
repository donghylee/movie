import base64
import uuid
from datetime import datetime

import requests
from flask import Blueprint, render_template, request, g, jsonify, session, redirect, url_for

from movie import db
from movie.filter import korean_days
from movie.models import Schedule, Reservation
from movie.views.auth_views import login_required

bp = Blueprint('payment', __name__, url_prefix='/payment')

TICKET_PRICE = 13000  # 1인당 임시 고정 단가 (가격 정책 테이블 없음)
FIXED_BG_CARD_NUMBER = '1234-5678-9101'  # 연습용 고정 카드번호 (모든 계정 동일)
FIXED_BG_POINT_PASSWORD = '1234'  # 연습용 고정 BG.POINT 비밀번호 (모든 계정 동일, 신규 가입자 포함)

# 토스페이먼츠 공식 문서에 공개된 v2 결제위젯(Payment Window) 전용 샌드박스 테스트 키
# (가입 없이 테스트 가능, 실제 결제 발생 안 함)
# 참고: https://docs.tosspayments.com/sdk/v2/js/payment-widget
TOSS_CLIENT_KEY = 'test_gck_docs_Ovk5rk1EwkEbP0W43n07xlzm'
TOSS_SECRET_KEY = 'test_gsk_docs_OaPz8L5KdmQXkzRz3y47BMw6'
TOSS_CONFIRM_URL = 'https://api.tosspayments.com/v1/payments/confirm'


@bp.after_app_request
def add_header(response):
    """This runs globally for ALL routes across all files."""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response


def _build_payment_context():
    schedule_id = session.get('schedule_id') or request.args.get('schedule_id', type=int)

    seats = session.get('seats')
    if seats is None:
        seats_param = request.args.get('seats', default='', type=str)
        seats = [s for s in seats_param.split(',') if s]

    schedule = Schedule.query.get_or_404(schedule_id) if schedule_id else None
    showtime = f'{schedule.showtime.strftime('%Y-%m-%d')} ({korean_days(schedule.showtime.strftime("%A"))}) {schedule.showtime.strftime('%H:%M')}'
    tickets = session.get('tickets')

    if tickets and schedule:
        adult = int(tickets.get('adult') or 0)
        child = int(tickets.get('child') or 0)
        senior = int(tickets.get('senior') or 0)
        disabled = int(tickets.get('disabled') or 0)
        audience_count = adult + child + senior + disabled
        amount = (
            adult * schedule.adult_price
            + child * schedule.child_price
            + senior * schedule.senior_price
            + disabled * schedule.disabled_price
        )
        max_ticket_price = max(
            (price for count, price in (
                (adult, schedule.adult_price),
                (child, schedule.child_price),
                (senior, schedule.senior_price),
                (disabled, schedule.disabled_price),
            ) if count > 0),
            default=0,
        )
    else:
        audience_count = request.args.get('count', default=len(seats) or 1, type=int)
        amount = TICKET_PRICE * audience_count
        max_ticket_price = TICKET_PRICE

    order_name = f'{schedule.movie.title} ({audience_count}매)' if schedule else '영화 예매'

    return {
        'schedule': schedule,
        'showtime': showtime,
        'seats': seats,
        'audience_count': audience_count,
        'amount': amount,
        'adult_price': schedule.adult_price if schedule else 0,
        'max_ticket_price': max_ticket_price,
        'point_balance': g.user.point if g.user else 0,
        'vip_coupon_count': g.user.vip_coupon_count if g.user else 0,
        'screening_voucher_count': g.user.screening_voucher_count if g.user else 0,
        'discount_coupon_count': g.user.discount_coupon_count if g.user else 0,
        'fixed_card_number': FIXED_BG_CARD_NUMBER,
        'order_id': uuid.uuid4().hex,
        'order_name': order_name,
    }


COUPON_COUNT_FIELDS = {
    'vip': 'vip_coupon_count',
    'voucher': 'screening_voucher_count',
    'discount': 'discount_coupon_count',
}


def _has_seat_conflict(context):
    schedule = context['schedule']
    if not schedule or not context['seats']:
        return False
    reserved_seats = set()
    for reservation in schedule.reservations:
        if reservation.canceled_at is None:
            reserved_seats.update(filter(None, reservation.seats.split(',')))
    return bool(reserved_seats & set(context['seats']))


def _deduct_coupon(coupon_type):
    field = COUPON_COUNT_FIELDS.get(coupon_type)
    if not field or not g.user:
        return
    current = getattr(g.user, field)
    if current > 0:
        setattr(g.user, field, current - 1)


def _save_reservation(context, payment, applied_points, coupon_discount, coupon_type):
    if not g.user or not context['schedule']:
        return
    db.session.add(Reservation(
        user_id=g.user.id,
        schedule_id=context['schedule'].id,
        seats=','.join(context['seats']),
        audience_count=context['audience_count'],
        order_id=payment['orderId'],
        order_amount=payment['totalAmount'] + applied_points + coupon_discount,
        discount_amount=applied_points + coupon_discount,
        total_amount=payment['totalAmount'],
        applied_points=applied_points,
        coupon_type=coupon_type or None,
        method=payment.get('method'),
    ))


@bp.route('/', methods=['GET'])
@login_required
def index():
    if not session.get('schedule_id') or not session.get('seats') or not session.get('tickets'):
        return redirect(url_for('booking.index'))
    return render_template(
        'payment/payment_main.html',
        toss_client_key=TOSS_CLIENT_KEY,
        customer_key=f'user-{g.user.id}' if g.user else '',
        **_build_payment_context(),
    )


@bp.route('/verify-password', methods=['POST'])
def verify_password():
    if not g.user:
        return jsonify({'valid': False}), 401

    password = request.form.get('password', '')
    valid = password == FIXED_BG_POINT_PASSWORD
    return jsonify({'valid': valid})


@bp.route('/deduct-points', methods=['POST'])
def deduct_points():
    if not g.user:
        return jsonify({'success': False}), 401

    points = request.form.get('points', default=0, type=int)
    if points < 0 or points > g.user.point:
        return jsonify({'success': False, 'point_balance': g.user.point}), 400

    g.user.point -= points
    db.session.commit()
    return jsonify({'success': True, 'point_balance': g.user.point})


@bp.route('/mock-complete')
@login_required
def mock_complete():
    order_id = request.args.get('orderId')
    amount = request.args.get('amount', type=int)
    method = request.args.get('method', default='')
    applied_points = request.args.get('appliedPoints', default=0, type=int)
    coupon = request.args.get('coupon', default='')
    coupon_discount = request.args.get('couponDiscount', default=0, type=int)

    context = _build_payment_context()

    if _has_seat_conflict(context):
        return render_template(
            'payment/payment_complete.html',
            success=False,
            error={
                'code': 'SEAT_CONFLICT',
                'message': '선택하신 좌석 중 일부가 이미 예약되어 결제가 진행되지 않았습니다. 좌석을 다시 선택해 주세요.',
            },
        )

    payment = {
        'orderId': order_id,
        'method': method,
        'totalAmount': amount,
        'approvedAt': datetime.now().strftime('%Y-%m-%d %H:%M'),
    }

    if g.user and 0 < applied_points <= g.user.point:
        g.user.point -= applied_points
    _deduct_coupon(coupon)
    _save_reservation(context, payment, applied_points, coupon_discount, coupon)
    if g.user:
        db.session.commit()
        session.pop('schedule_id', None)
        session.pop('seats', None)
        session.pop('tickets', None)

    return render_template(
        'payment/payment_complete.html',
        success=True,
        payment=payment,
        applied_points=applied_points,
        coupon_discount=coupon_discount,
        schedule=context['schedule'],
        showtime=context['showtime'],
        seats=context['seats'],
        audience_count=context['audience_count'],
    )


@bp.route('/toss/success')
@login_required
def toss_success():
    payment_key = request.args.get('paymentKey')
    order_id = request.args.get('orderId')
    amount = request.args.get('amount', type=int)
    applied_points = request.args.get('appliedPoints', default=0, type=int)
    coupon = request.args.get('coupon', default='')
    coupon_discount = request.args.get('couponDiscount', default=0, type=int)

    context = _build_payment_context()

    if _has_seat_conflict(context):
        return render_template(
            'payment/payment_complete.html',
            success=False,
            error={
                'code': 'SEAT_CONFLICT',
                'message': '선택하신 좌석 중 일부가 이미 예약되어 결제가 진행되지 않았습니다. 좌석을 다시 선택해 주세요.',
            },
        )

    auth = base64.b64encode(f'{TOSS_SECRET_KEY}:'.encode()).decode()
    res = requests.post(
        TOSS_CONFIRM_URL,
        json={'paymentKey': payment_key, 'orderId': order_id, 'amount': amount},
        headers={
            'Authorization': f'Basic {auth}',
            'Content-Type': 'application/json',
        },
    )

    if res.status_code == 200:
        payment = res.json()
        payment['approvedAt'] = datetime.fromisoformat(payment['approvedAt']).strftime('%Y-%m-%d %H:%M')

        if g.user and 0 < applied_points <= g.user.point:
            g.user.point -= applied_points
        _deduct_coupon(coupon)
        _save_reservation(context, payment, applied_points, coupon_discount, coupon)
        if g.user:
            db.session.commit()
            session.pop('schedule_id', None)
            session.pop('seats', None)
            session.pop('tickets', None)

        return render_template(
            'payment/payment_complete.html',
            success=True,
            payment=payment,
            applied_points=applied_points,
            coupon_discount=coupon_discount,
            schedule=context['schedule'],
            showtime=context['showtime'],
            seats=context['seats'],
            audience_count=context['audience_count'],
        )

    return render_template('payment/payment_complete.html', success=False, error=res.json())


@bp.route('/toss/fail')
@login_required
def toss_fail():
    error = {
        'code': request.args.get('code'),
        'message': request.args.get('message'),
    }
    return render_template('payment/payment_complete.html', success=False, error=error)
