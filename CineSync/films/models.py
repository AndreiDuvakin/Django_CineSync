from django.db.models import Model, CharField, IntegerField, DateField, ManyToManyField
from django.core.validators import MinValueValidator


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
