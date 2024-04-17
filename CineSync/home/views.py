import datetime
from datetime import date
from collections import defaultdict
from pprint import pprint
from random import shuffle

from django.db.models import QuerySet
from django.http import HttpResponse
from django.shortcuts import render

from films.models import Film
from timetable.models import FilmSession


def homepage(request):
    films = Film.objects.on_main()
    film_sessions = FilmSession.objects.nearest_timetable()
    sessions_by_date_and_film = defaultdict(lambda: defaultdict(list))

    for session in film_sessions:
        session_date = session.start_datetime.date()
        sessions_by_date_and_film[session_date][session.film].append(session)

    for session in film_sessions:
        session_date = session.start_datetime.date()
        sessions_by_date_and_film[session_date] = dict(sessions_by_date_and_film[session_date])

    template = render(
        request,
        'home/homepage.html',
        context={
            'films_preview': films,
            'films_sessions': dict(sessions_by_date_and_film),
            'tomorrow': date.today() + datetime.timedelta(days=1)
        }
    )
    return HttpResponse(
        template,
    )
