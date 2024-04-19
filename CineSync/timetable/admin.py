from django.contrib import admin

from timetable.models import Auditorium, Row, FilmSession


@admin.register(Auditorium)
class AuditoriumAdmin(admin.ModelAdmin):
    list_display = [
        Auditorium.number.field.name,
    ]


@admin.register(Row)
class RowAdmin(admin.ModelAdmin):
    list_display = [
        Row.row_number.field.name,
    ]


@admin.register(FilmSession)
class FilmSessionAdmin(admin.ModelAdmin):
    list_display = [
        FilmSession.start_datetime.field.name,
        FilmSession.film.field.name,
    ]
