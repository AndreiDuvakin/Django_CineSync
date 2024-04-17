import time
from datetime import timedelta

from django.db.models import (
    Model,
    CharField,
    IntegerField,
    DateField,
    ManyToManyField,
    Manager, ImageField,
)
from django.utils import timezone
from django.core.validators import MinValueValidator
from sorl.thumbnail import get_thumbnail


class FilmManager(Manager):
    def released(self):
        return super().get_queryset().filter(
            release_date__lt=timezone.now(),
        )

    def on_main(self):
        current_datetime = timezone.now()
        end_datetime = current_datetime + timedelta(days=5)
        films_with_sessions = super().get_queryset().filter(
            sessions__start_datetime__gte=current_datetime,
            sessions__start_datetime__lte=end_datetime,
        ).exclude(image=None).distinct().only(
            Film.name.field.name,
            Film.image.field.name,
            Film.description.field.name,
        )

        if films_with_sessions.count() > 5:
            films_with_sessions = films_with_sessions[:5]
        elif films_with_sessions.count() > 0:
            films_with_sessions = films_with_sessions[:films_with_sessions.count()]
        return films_with_sessions


class Genre(Model):
    name = CharField(
        'Название',
        help_text='Название жанра',
        max_length=100,
        null=False,
    )

    class Meta:
        db_table = 'films_genres'
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Film(Model):
    def get_upload_path(self, filename):
        return f'users/films/{self.pk}/{time.time()}_{filename}'

    def get_image_url(self):
        return self.image.url

    objects = FilmManager()

    name = CharField(
        'Название',
        help_text='Название фильма',
        max_length=100,
        null=False,
    )

    duration = IntegerField(
        'Продолжительность',
        help_text='Продолжительность фильма (в минутах)',
        validators=[MinValueValidator(0)],
        null=False,
    )

    release_date = DateField(
        'Дата релиза',
        help_text='Дата выхода фильма',
    )

    description = CharField(
        help_text='Описание фильма',
        max_length=1000,
        null=False,
    )

    image = ImageField(
        null=True,
        blank=True,
        verbose_name='Изображение фильма',
        upload_to=get_upload_path,
    )

    genres = ManyToManyField(
        Genre,
        verbose_name='Жанры',
        related_name='films',
        related_query_name='films',
        help_text='Жанры фильма',
    )

    class Meta:
        db_table = 'films_films'
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
