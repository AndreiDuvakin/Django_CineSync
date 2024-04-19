from django.urls import path

from tickets.views import ticket_view

app_name = 'tickets'

urlpatterns = [
    path('', ticket_view, name='tickets'),
]