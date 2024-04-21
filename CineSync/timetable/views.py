import datetime
from datetime import date

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone

from timetable.models import FilmSession, Row
from timetable.forms import SeatSelectionForm
from tickets.models import Order, Ticket


def timetable_view(request):
    film_sessions = FilmSession.objects.all_timetable()
    sessions_by_date_and_film = {}

    for session in film_sessions:
        session_date = session.start_datetime.date()
        if session_date not in sessions_by_date_and_film:
            sessions_by_date_and_film[session_date] = {}
        film_sessions_for_date = sessions_by_date_and_film[session_date]
        if session.film not in film_sessions_for_date:
            film_sessions_for_date[session.film] = []
        film_sessions_for_date[session.film].append(session)

    for session_date, session_films in sessions_by_date_and_film.items():
        for session_film in session_films:
            sessions_by_date_and_film[session_date][session_film].sort(
                key=lambda sorted_session: sorted_session.start_datetime,
            )
    template = render(
        request,
        'timetable/timetable.html',
        context={
            'films_sessions': sessions_by_date_and_film,
            'today': date.today(),
            'tomorrow': date.today() + datetime.timedelta(days=1),
        }
    )
    return HttpResponse(
        template,
    )


@login_required
def session_view(request, sess_id):
    session = get_object_or_404(
        FilmSession.objects.select_related(
            'film',
            'auditorium',
        ).prefetch_related(
            'auditorium__rows',
            'film__genres',
        ),
        id=sess_id,
    )
    height = round(session.auditorium.rows.count() * 4 + 7)

    tickets = Ticket.objects.get_tickets_for_session(session.pk)
    occupied_seats = [f"{str(ticket.row_number)}-{str(ticket.column_number)}" for ticket in tickets]

    if request.method == 'POST':
        form = SeatSelectionForm(request.POST, auditorium=session.auditorium)
        if form.is_valid():
            with transaction.atomic():
                selected_seats = form.clean_selected_seats()
                user_profile = request.user.profile

                order = Order.objects.create(
                    session=session,
                    profile=user_profile,
                    datetime_order=timezone.now(),
                )

                for seat in selected_seats:
                    Ticket.objects.create(
                        order=order,
                        row_number=seat[0],
                        column_number=seat[1],
                    )

                return redirect(reverse('home:homepage'))
    else:
        form = SeatSelectionForm(auditorium=session.auditorium)

    context = {
        'session': session,
        'height': height,
        'form': form,
        'occupied_seats': occupied_seats,
    }
    template = 'timetable/session.html'
    return render(request, template, context)
