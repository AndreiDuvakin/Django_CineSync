from django.urls import path

from tickets.views import order_success, my_orders

app_name = 'tickets'

urlpatterns = [
    path('order/success', order_success, name='order_success'),
    path('my/', my_orders, name='my_orders')
]
