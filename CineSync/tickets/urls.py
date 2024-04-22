from django.urls import path

from tickets.views import my_orders, order_success

app_name = 'tickets'

urlpatterns = [
    path('order/success', order_success, name='order_success'),
    path('my/', my_orders, name='my_orders'),
]
