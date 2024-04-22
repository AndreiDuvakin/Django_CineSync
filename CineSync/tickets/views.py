from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from tickets.models import Order


def order_success(request):
    return render(request, 'tickets/order_success.html')


@login_required
def my_orders(request):
    user = request.user
    queryset = Order.objects.filter(profile__id=user.profile.id)
    queryset = queryset.select_related('session', 'session__film')
    queryset = queryset.prefetch_related('tickets')
    orders = queryset.order_by('-datetime_order')

    context = {
        'my_orders': orders,
    }
    template = 'tickets/my_orders.html'

    return render(request, template, context)
