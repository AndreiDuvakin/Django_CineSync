from django.db.models import ForeignKey, CASCADE, Model, IntegerField, DateField
from django.core.validators import MinValueValidator

from timetable.models import FilmSession
from users.models import Profile


class Order(Model):
    session = ForeignKey(
        FilmSession,
        on_delete=CASCADE,
        related_name='orders',
        related_query_name='orders',
    )

    profile = ForeignKey(
        Profile,
        on_delete=CASCADE,
        related_name='orders',
        related_query_name='orders',
    )

    datetime_order = DateField(
        verbose_name='Дата и время оформления заказа',
        help_text='Дата и время оформления заказа',
    )

    class Meta:
        db_table = 'tickets_orders'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Ticket(Model):
    order = ForeignKey(
        Order,
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

    class Meta:
        db_table = 'tickets_tickets'
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'
