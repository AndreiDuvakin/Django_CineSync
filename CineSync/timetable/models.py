from django.db.models import Model, CharField, IntegerField, OneToOneField, CASCADE
from django.core.validators import MinValueValidator


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


class Rows(Model):
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
    auditorium = OneToOneField(
        Auditorium,
        on_delete=CASCADE,
        verbose_name='зал',
        related_name='rows',
    )

    class Meta:
        db_table = 'timetable_rows'
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
