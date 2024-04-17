from datetime import timedelta

from django.db.models import Model, CharField, IntegerField, CASCADE, DateTimeField, FloatField, ForeignKey
from django.core.validators import MinValueValidator

from films.models import Film


class Auditorium(Model):
    number = CharField(
        max_length=20,
        verbose_name='Номер кинозала',
    )

    row_count = IntegerField(
        verbose_name='Количество рядов кресел в зале',
        validators=[
            MinValueValidator(1),
        ],
    )

    class Meta:
        db_table = 'timetable_auditoriums'
        verbose_name = 'Зал'
        verbose_name_plural = 'Залы'


class Row(Model):
    row_number = IntegerField(
        verbose_name='Номер ряда',
        validators=[
            MinValueValidator(1),
        ],
    )

    column_count = IntegerField(
        verbose_name='Количество кресел в ряду',
        validators=[
            MinValueValidator(1),
        ],
    )

    auditorium = ForeignKey(
        Auditorium,
        on_delete=CASCADE,
        verbose_name='Зал',
        related_name='rows',
        related_query_name='rows',
    )

    class Meta:
        db_table = 'timetable_rows'
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class FilmSession(Model):
    start_datetime = DateTimeField(
        verbose_name='Дата и время начала сеанса',
    )

    end_datetime = DateTimeField(
        verbose_name='Дата и время начала сеанса',
        blank=True,
        null=True,
    )


    price = FloatField(
        verbose_name='Цена билета',
        validators=[
            MinValueValidator(1),
        ],
    )

    film = ForeignKey(
        Film,
        on_delete=CASCADE,
        verbose_name='Фильм',
        related_name='sessions',
        related_query_name='sessions',
    )
    auditorium = ForeignKey(
        Auditorium,
        on_delete=CASCADE,
        verbose_name='Зал',
        related_name='sessions',
        related_query_name='sessions',
    )

    def save(self, *args, **kwargs):
        if self.start_datetime and self.film.duration:
            self.end_datetime = self.start_datetime + timedelta(minutes=self.film.duration)
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'timetable_film_sessions'
        verbose_name = 'Сеанс'
        verbose_name_plural = 'Сеансы'
