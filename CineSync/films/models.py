import time
from datetime import timedelta

import sorl
from django.db.models import (
    Model,
    CharField,
    IntegerField,
    DateField,
    ManyToManyField,
    Manager, ImageField, Min,
)
from django.utils import timezone
from django.core.validators import MinValueValidator
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail


class FilmManager(Manager):
    def released(self):
        return super().get_queryset().filter(
            release_date__lt=timezone.now(),
        )

    def will_be_shown(self):
        current_datetime = timezone.now()
        films_with_sessions = super().get_queryset().filter(
            sessions__start_datetime__gte=current_datetime,
        ).annotate(
            nearest_session=Min('sessions__start_datetime')
        ).order_by('nearest_session')

        return films_with_sessions

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

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'films_genres'
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Film(Model):
    def __str__(self):
        return self.name

    def get_upload_path(self, filename):
        return f'users/films/{self.pk}/{time.time()}_{filename}'

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

    def get_image_300x300(self):
        return sorl.thumbnail.get_thumbnail(
            self.image,
            "300x300",
            crop="center",
            quality=51,
        )

    def image_tmb(self):
        if self.image:
            tag = f"{self.get_image_300x300().url}"
            return mark_safe(tag)

        return "Нет изорбражения"

    image_tmb.field_name = "image_tmb"
    image_tmb.allow_tags = True
    image_tmb.short_description = "Превью"

    class Meta:
        db_table = 'films_films'
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
