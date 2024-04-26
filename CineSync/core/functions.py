from timetable.models import FilmSession


def get_film_to_sessions():
    film_sessions = FilmSession.objects.nearest_timetable()
    sessions_by_date_and_film = {}

    for session in film_sessions:
        session_date = session.start_datetime.date()
        session_film = session.film
        sessions_by_date_and_film.setdefault(session_date, {}).setdefault(session_film, []).append(session)

    for session_date in sessions_by_date_and_film:
        for session_film in sessions_by_date_and_film[session_date]:
            sessions_by_date_and_film[session_date][session_film].sort(key=lambda x: x.start_datetime)

    return sessions_by_date_and_film
