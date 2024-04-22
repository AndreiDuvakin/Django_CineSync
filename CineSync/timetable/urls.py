from django.urls import path

from timetable.views import session_view, timetable_view

app_name = 'time_table'

urlpatterns = [
    path('', timetable_view, name='main'),
    path('session/<int:sess_id>', session_view, name='session'),
]
