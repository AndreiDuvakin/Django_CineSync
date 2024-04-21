from django.urls import path

from tickets.views import ticket_view, order_success

app_name = 'tickets'

urlpatterns = [
    path('', ticket_view, name='tickets'),
    path('/order/success', order_success, name='order_success'),
]
