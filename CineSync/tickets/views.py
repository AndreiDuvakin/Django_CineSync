from django.shortcuts import render, get_object_or_404


def ticket_view(request):
    return render(request, 'tickets/ticket_buy.html')
