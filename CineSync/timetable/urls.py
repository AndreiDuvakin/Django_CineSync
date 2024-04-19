from django.urls import path

from timetable.views import timetable_view, session_view

app_name = 'time_table'

urlpatterns = [
    path('', timetable_view, name='main'),
    path('session/<int:pk>', session_view, name='main'),
]
