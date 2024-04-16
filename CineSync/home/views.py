from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    template = render(
        request,
        'home/homepage.html'
    )
    return HttpResponse(
        template,
    )
