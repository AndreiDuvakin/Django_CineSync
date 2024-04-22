from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_list_or_404

from tickets.models import Order, Ticket


def ticket_view(request):
    return render(request, 'tickets/ticket_buy.html')


def order_success(request):
    return render(request, 'tickets/order_success.html')


@login_required
def my_orders(request):
    user = request.user
    orders = get_list_or_404(
        Order.objects.filter(
            profile__id=user.profile.id,
        ).select_related(
            'session',
            'session__film',
        ).prefetch_related(
            'tickets',
        ).order_by(
            '-datetime_order'
        )
    )
    context = {
        'my_orders': orders,
    }
    template = 'tickets/my_orders.html'

    return render(request, template, context)
