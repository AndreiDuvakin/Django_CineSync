from django.http import HttpResponse
from django.shortcuts import render

from films.models import Film


def homepage(request):
    films = Film.objects.on_main()
    template = render(
        request,
        'home/homepage.html',
        context={
            'films_preview': films
        }
    )
    return HttpResponse(
        template,
    )
