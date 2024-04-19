from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from films.models import Film


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
    return render(
        request,
        'films/film_details.html',
        {'item': item},
    )

