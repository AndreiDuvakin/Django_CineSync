from django.conf import settings
from django.db.models import Model, OneToOneField, CASCADE, DateField, CharField


class Profile(Model):
    user = OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name='пользователь',
        related_name='profile',
        related_query_name='profile',
        on_delete=CASCADE,
    )
    birthday = DateField(
        null=True,
        blank=True,
    )
    role = CharField(
        verbose_name='роль пользователя',
    )
