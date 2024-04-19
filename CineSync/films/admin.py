from django.contrib import admin
from django.utils.safestring import mark_safe

from films.models import Film, Genre


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = [
        Film.name.field.name,
        Film.duration.field.name,
        'get_image',
    ]

    readonly_fields = ("get_image",)

    filter_horizontal = [
        Film.genres.field.name,
    ]

    def get_image(self, obj):
        return mark_safe(
            f"<img src='{obj.image_tmb()}' width='50' height='50'",
        )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = [
        Genre.name.field.name,
    ]
