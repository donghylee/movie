from flask import Blueprint, render_template, request, redirect, url_for, session
from datetime import datetime, timedelta, time
import re

from movie.filter import korean_days
from movie.models import Theater, Auditorium, Schedule
from movie.views.auth_views import login_required

from sqlalchemy import func
bp = Blueprint('booking', __name__, url_prefix='/booking')


@bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    try:
        if request.method == 'POST':
            session['schedule_id'] = int(request.form.get('selected_schedule'))
            return redirect(url_for('booking.seats'))
    except:
        print(request.form.get('selected_schedule'))

    regions_query = Theater.query.with_entities(Theater.region, func.count(Theater.region)).group_by(Theater.region).order_by(Theater.id).all()
    regions = []
    for region in regions_query:
        regions.append({
            'name': region[0],
            'theater_count': region[1]
        })
    theaters = get_theaters('서울')

    import holidays
    current_date = datetime.now()
    datepicker = []
    months = []
    for i in range(5):
        week = []
        for j in range(7):
            date = {
                'month': '',
                'date': current_date.strftime("%d"),
                'day': korean_days(current_date.strftime("%A")),
                'full_date': current_date.strftime("%Y-%m-%d"),
                'is_red': True if current_date.date() in holidays.KR(years=current_date.year).keys() or korean_days(current_date.strftime("%A")) in ['토', '일'] else False
            }
            if i == 0 and j == 0:
                date['day'] = '오늘'
            if current_date.strftime("%m") not in months:
                date['month'] = f'{current_date.strftime("%m")}월'
                months.append(current_date.strftime("%m"))
            week.append(date)
            current_date = current_date + timedelta(days=1)
        datepicker.append(week)

    return render_template(
        'booking/booking_main.html',
        regions=regions,
        datepicker=datepicker,
        theaters=theaters
    )


@bp.route('/theaters/<path:region>')
def get_theaters(region):
    theaters = []
    theaters_query = Theater.query.filter_by(region=region).all()
    for theater in theaters_query:
        theaters.append({
            'id': theater.id,
            'name': theater.name
        })

    return theaters


@bp.route('/movies/<int:theater_id>')
def get_movies(theater_id):
    if theater_id is None:
        return []

    queried_theater = Theater.query.filter_by(id=theater_id).first()
    queried_movies = {}
    if queried_theater:
        queried_movies = {
            schedule.movie
            for auditorium in queried_theater.auditoriums
            for schedule in auditorium.schedules
            if schedule.movie is not None
        }

    movies = []
    for movie in queried_movies:
        movies.append({
            'id': str(movie.id),
            'title': movie.title,
            'poster_url': movie.poster_url,
            'rating': movie.rating,
            'runtime': movie.runtime,
            'created_at': movie.created_at.strftime("%Y-%m-%d"),
        })
    movies = sorted(movies, key=lambda x: x['title'])

    return movies


@bp.route('/schedules/<int:theater_id>/<int:movie_id>/<path:selected_date>')
def get_schedules(theater_id, movie_id, selected_date):
    if theater_id is None or movie_id is None or selected_date is None:
        return []
    current_date = datetime.now()

    try:
        datetime.strptime(selected_date, "%Y-%m-%d")
    except ValueError:
        selected_date = current_date.strftime("%Y-%m-%d")
    if datetime.strptime(selected_date, "%Y-%m-%d") < current_date:
        selected_date = current_date.strftime("%Y-%m-%d")
    theaters = []

    queried_theater = Theater.query.filter_by(id=theater_id).first()
    queried_schedules = {}
    if queried_theater:
        if movie_id != '':
            if selected_date == str(datetime.now().date()):
                start_time = datetime.now()
            else:
                start_time = datetime.strptime(selected_date, "%Y-%m-%d")
            end_time = datetime.combine(datetime.strptime(selected_date, "%Y-%m-%d"), time.max)
            queried_schedules = Schedule.query.join(
                Auditorium, Schedule.auditorium
            ).filter(
                Auditorium.theater_id == queried_theater.id,
                Schedule.movie_id == movie_id,
                Schedule.showtime.between(start_time, end_time)
            ).all()

    schedules = []
    for schedule in queried_schedules:
        taken_seats = []
        for reservation in schedule.reservations:
            if reservation.canceled_at is None:
                seats = reservation.seats.split(',')
                seats = list(filter(None, seats))
                taken_seats += seats
        schedules.append({
            'id': str(schedule.id),
            'auditorium': schedule.auditorium.name,
            'total_seats': schedule.auditorium.total_seats,
            'remaining_seats': schedule.auditorium.total_seats - len(taken_seats),
            'showtime': schedule.showtime.strftime("%H:%M")
        })
    schedules = sorted(schedules, key=lambda x: x['showtime'])

    return schedules


@bp.route('/seats', methods=['GET', 'POST'])
@login_required
def seats():
    schedule_id = session.get('schedule_id')
    if schedule_id is None:
        return redirect(url_for('booking.index'))

    queried_schedule = Schedule.query.filter_by(id=schedule_id).first()

    reserved_seats = []
    for reservation in queried_schedule.reservations:
        if reservation.canceled_at is None:
            reservation_seats = reservation.seats.split(',')
            reservation_seats = list(filter(None, reservation_seats))
            reserved_seats += reservation_seats

    try:
        if request.method == 'POST':
            seats = request.form.get('booking_seats').split(',')
            seats = list(filter(None, seats))

            def natural_sort_key(s):
                return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

            seats = sorted(seats, key=natural_sort_key)

            if set(seats) & set(reserved_seats):
                return redirect(url_for('booking.seats', conflict=1))

            tickets = {
                'adult': request.form.get('adult_tickets'),
                'child': request.form.get('child_tickets'),
                'senior': request.form.get('senior_tickets'),
                'disabled': request.form.get('disabled_tickets')
            }
            session['seats'] = seats
            session['tickets'] = tickets
            return redirect(url_for('payment.index'))
    except:
        print(request.form.get('booking_seats'))

    showtime_date = f'{queried_schedule.showtime.strftime("%Y.%m.%d")} ({korean_days(queried_schedule.showtime.strftime("%A"))})'
    end_time = queried_schedule.showtime + timedelta(minutes=queried_schedule.movie.runtime)
    showtime_time = f'{queried_schedule.showtime.strftime("%H:%M")} ~ {end_time.strftime("%H:%M")}'
    auditorium = f'{queried_schedule.auditorium.theater.name} {queried_schedule.auditorium.name}'
    schedule = {
        'id': queried_schedule.id,
        'title': queried_schedule.movie.title,
        'poster_url': queried_schedule.movie.poster_url,
        'rating': queried_schedule.movie.rating.lower(),
        'showtime_date': showtime_date,
        'showtime_time': showtime_time,
        'auditorium': auditorium,
        'seat_layout': queried_schedule.auditorium.seat_layout,
        'reserved_seats': reserved_seats,
        'remaining_seats': queried_schedule.auditorium.total_seats - len(reserved_seats),
        'adult_price': queried_schedule.adult_price,
        'child_price': queried_schedule.child_price,
        'senior_price': queried_schedule.senior_price,
        'disabled_price': queried_schedule.disabled_price
    }

    return render_template(
        'booking/booking_seat.html', schedule=schedule, seat_conflict=request.args.get('conflict') == '1'
    )