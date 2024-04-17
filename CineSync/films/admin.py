from django.contrib import admin

from films.models import Film, Genre


@admin.register(Film)
class ItemAdmin(admin.ModelAdmin):
    list_display = [
        Film.name.field.name,
        Film.duration.field.name,
    ]

    filter_horizontal = [
        Film.genres.field.name,
    ]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = [
        Genre.name.field.name,
    ]
