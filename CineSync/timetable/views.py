import datetime
from datetime import date

from django.http import HttpResponse
from django.shortcuts import render
from films.models import Film

from timetable.models import FilmSession


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


def session_view(request):
    template = 'session/session_details.html'
    return render(request, template)
