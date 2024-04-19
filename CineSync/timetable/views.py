from django.shortcuts import render
from films.models import Film


def timetable_view(request):
    films = Film.objects.all()
    template = 'timetable/timetable.html'
    context = {'films': films}
    return render(request, template, context)


def session_view(request):
    template = 'session/session_details.html'
    return render(request, template)
