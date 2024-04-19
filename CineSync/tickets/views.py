from django.shortcuts import render, get_object_or_404
from timetable.models import FilmSession


def ticket_view(request, sess_id):
    session = get_object_or_404(
        FilmSession.objects.all(),
        id=sess_id,
    )
    context = {'session': session}
    return render(request, 'tickets/ticket_buy.html', context)
