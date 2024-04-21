from django.shortcuts import render, get_object_or_404


def ticket_view(request):
    return render(request, 'tickets/ticket_buy.html')


def order_success(request):
    return render(request, 'tickets/order_success.html')
