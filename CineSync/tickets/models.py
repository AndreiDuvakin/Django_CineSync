from django.db import models
from django.core.validators import MinValueValidator

from timetable.models import FilmSessions
from users.models import Profile


class Ticket(models.Model):
    session_id = models.ForeignKey(
        FilmSessions,
        on_delete=models.CASCADE,
        related_name='tickets',
        related_query_name='tickets',
    )

    user_id = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='tickets',
        related_query_name='tickets',
    )

    row_number = models.IntegerField(
        'Номер ряда',
        null=False,
        validators=[MinValueValidator(1)],
        help_text='Номер ряда',
    )

    column_number = models.IntegerField(
        'Номер кресла',
        null=False,
        validators=[MinValueValidator(1)],
        help_text='Номер кресла в ряду',
    )
