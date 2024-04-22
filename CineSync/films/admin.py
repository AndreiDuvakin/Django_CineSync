from django.contrib import admin
from django.utils.safestring import mark_safe

from films.models import Actor, Country, Director, Film, Genre


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = [
        Film.name.field.name,
        Film.duration.field.name,
        Film.image.field.name,
        'get_image',
    ]

    readonly_fields = ('get_image',)

    filter_horizontal = [
        Film.genres.field.name,
        Film.directors.field.name,
        Film.countries.field.name,
        Film.actors.field.name,
    ]

    list_editable = [
        Film.image.field.name,
    ]

    def get_image(self, obj):
        return mark_safe(
            f'<img src="{obj.image_tmb()}" width="50" height="50"',
        )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = [
        Genre.name.field.name,
    ]


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = [
        Actor.first_name.field.name,
        Actor.last_name.field.name,
    ]


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = [
        Director.first_name.field.name,
        Director.last_name.field.name,
    ]


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = [
        Country.name.field.name,
    ]
