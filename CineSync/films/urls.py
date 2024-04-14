from django.urls import path

from films import views

app_name = 'films'
urlpatterns = [
    path('', views.films_list, name='main'),
    path('<int:film_id>/', views.film_details, name='film_details')
]
