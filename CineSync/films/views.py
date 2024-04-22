from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from films.models import Film
from timetable.models import FilmSession


def films_list(request: HttpResponse) -> HttpResponse:
    films = Film.objects.will_be_shown()
    return render(
        request,
        'films/films_list.html',
        {'films': films},
    )


def film_details(request: HttpResponse, film_id: int) -> HttpResponse:
    item = get_object_or_404(
        Film.objects.released(),
        id=film_id,
    )
    film_sessions = FilmSession.objects.nearest_timetable().filter(
        film_id=film_id,
    )
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

    context = {
        'film_sessions': sessions_by_date_and_film,
        'item': item,
    }
    return render(
        request,
        'films/film_details.html',
        context,
    )
