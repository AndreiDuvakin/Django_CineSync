from django.db import models
from django.core.validators import MinValueValidator


class Genre(models.Model):
    name = models.CharField(
        'Название',
        help_text='Название жанра',
        max_length=100,
        null=False,
    )

    class Meta:
        db_table = 'films_genres'
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Film(models.Model):
    name = models.CharField(
        'Название',
        help_text='Название фильма',
        max_length=100,
        null=False,
    )

    duration = models.IntegerField(
        'Продолжительность',
        help_text='Продолжительность фильма (в минутах)',
        validators=[MinValueValidator(0)],
        null=False,
    )

    release_date = models.DateField(
        'Дата релиза',
        help_text='Дата выхода фильма',
    )

    genres = models.ManyToManyField(
        Genre,
        verbose_name='Жанры',
        related_name='films',
        help_text='Жанры фильма',
    )

    class Meta:
        db_table = 'films_films'
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
