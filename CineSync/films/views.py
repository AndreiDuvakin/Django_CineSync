from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from films.models import Film
from core.functions import get_film_to_sessions


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
    sessions_by_date_and_film = get_film_to_sessions()

    context = {
        'film_sessions': sessions_by_date_and_film,
        'item': item,
    }
    return render(
        request,
        'films/film_details.html',
        context,
    )
