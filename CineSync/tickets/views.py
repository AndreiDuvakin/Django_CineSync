from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from tickets.models import Order, Ticket


def ticket_view(request):
    return render(request, 'tickets/ticket_buy.html')


def order_success(request):
    return render(request, 'tickets/order_success.html')


@login_required
def my_orders(request):
    user = request.user
    orders = get_object_or_404(
        Order.objects.filter(
            profile__id=user.profile.id,
        ).prefetch_related(
            'tickets',
        )
    )
    return render(request, 'tickets/my_orders.html')
