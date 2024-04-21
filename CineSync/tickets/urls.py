from django.urls import path

from tickets.views import ticket_view, order_success, my_orders

app_name = 'tickets'

urlpatterns = [
    path('', ticket_view, name='tickets'),
    path('order/success', order_success, name='order_success'),
    path('my/', my_orders, name='my_orders')
]
