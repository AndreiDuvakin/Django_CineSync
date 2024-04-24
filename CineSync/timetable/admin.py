from django.contrib import admin

from timetable.models import Auditorium, FilmSession, Row


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
        FilmSession.film.field.name,
        FilmSession.start_datetime.field.name,
    ]
    list_editable = [
        FilmSession.start_datetime.field.name,
    ]
