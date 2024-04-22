from django.urls import path

from films.views import film_details, films_list

app_name = 'films'
urlpatterns = [
    path('', films_list, name='main'),
    path('<int:film_id>/', film_details, name='film_details'),
]
