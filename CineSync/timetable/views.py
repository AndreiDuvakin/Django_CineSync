from django.shortcuts import render, get_object_or_404
from films.models import Film
from timetable.models import FilmSession, Row


def timetable_view(request):
    films = Film.objects.all()
    template = 'timetable/timetable.html'
    context = {'films': films}
    return render(request, template, context)


def session_view(request, sess_id):
    session = get_object_or_404(
        FilmSession.objects.all(),
        id=sess_id,
    )
    height = session.auditorium.row_count * 80 + 300
    context = {
        'session': session,
        'seats': Row.objects.filter(auditorium_id=session.auditorium.id),
        'height': height,
    }
    template = 'timetable/session.html'
    return render(request, template, context)
