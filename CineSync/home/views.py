import datetime
from datetime import date

from django.http import HttpResponse
from django.shortcuts import render

from films.models import Film
from core.functions import get_film_to_sessions


def homepage(request):
    films = Film.objects.on_main()
    sessions_by_date_and_film = get_film_to_sessions()
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
