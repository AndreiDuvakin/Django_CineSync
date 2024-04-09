from django.db.models import ForeignKey, CASCADE, Model, IntegerField
from django.core.validators import MinValueValidator

from timetable.models import FilmSession
from users.models import Profile


class Ticket(Model):
    session = ForeignKey(
        FilmSession,
        on_delete=CASCADE,
        related_name='tickets',
        related_query_name='tickets',
    )

    profile = ForeignKey(
        Profile,
        on_delete=CASCADE,
        related_name='tickets',
        related_query_name='tickets',
    )

    row_number = IntegerField(
        'Номер ряда',
        null=False,
        validators=[MinValueValidator(1)],
        help_text='Номер ряда',
    )

    column_number = IntegerField(
        'Номер кресла',
        null=False,
        validators=[MinValueValidator(1)],
        help_text='Номер кресла в ряду',
    )
