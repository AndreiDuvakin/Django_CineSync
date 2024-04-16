from django.urls import path

from films.views import films_list, film_details

app_name = 'time_table'

urlpatterns = [
    path('', films_list, name='main'),
]
