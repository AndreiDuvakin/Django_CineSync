import datetime
from datetime import date

from django.http import HttpResponse
from django.shortcuts import render

from films.models import Film
from timetable.models import FilmSession


def homepage(request):
    films = Film.objects.on_main()
    film_sessions = FilmSession.objects.nearest_timetable()
    sessions_by_date_and_film = {}

    for session in film_sessions:
        session_date = session.start_datetime.date()
        session_film = session.film
        sessions_by_date_and_film.setdefault(session_date, {}).setdefault(session_film, []).append(session)

    for session_date in sessions_by_date_and_film:
        for session_film in sessions_by_date_and_film[session_date]:
            sessions_by_date_and_film[session_date][session_film].sort(key=lambda x: x.start_datetime)

    template = render(
        request,
        'home/homepage.html',
        context={
            'films_preview': films,
            'films_sessions': sessions_by_date_and_film,
            'today': date.today(),
            'tomorrow': date.today() + datetime.timedelta(days=1),
        },
    )
    return HttpResponse(
        template,
    )
