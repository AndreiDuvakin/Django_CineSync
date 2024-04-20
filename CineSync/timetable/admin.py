from django.contrib import admin

from timetable.models import Auditorium, Row, FilmSession


class RowAdminInline(admin.StackedInline):
    model = Row


@admin.register(Auditorium)
class AuditoriumAdmin(admin.ModelAdmin):
    list_display = [
        Auditorium.number.field.name,
    ]
    inlines = [
        RowAdminInline,
    ]


@admin.register(FilmSession)
class FilmSessionAdmin(admin.ModelAdmin):
    list_display = [
        FilmSession.start_datetime.field.name,
        FilmSession.film.field.name,
    ]
