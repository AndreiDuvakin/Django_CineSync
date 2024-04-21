import time

from django.conf import settings
from django.db.models import Model, OneToOneField, CASCADE, DateField, CharField, ImageField, ManyToManyField
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail

from films.models import Genre


class Profile(Model):

    def get_upload_path(self, filename):
        return f'users/avatars/{self.user_id}/{time.time()}_{filename}'

    user = OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name='Пользователь',
        related_name='profile',
        related_query_name='profile',
        on_delete=CASCADE,
    )
    birthday = DateField(
        verbose_name='Дата рождения пользователя',
        null=True,
        blank=True,
    )
    role = CharField(
        verbose_name='Роль пользователя',
        max_length=20,
    )
    image = ImageField(
        null=True,
        blank=True,
        verbose_name='Аватар пользователя',
        upload_to=get_upload_path,
    )
    genres = ManyToManyField(
        Genre,
        related_name='profiles',
        related_query_name='profiles',
    )

    def __str__(self):
        return f'{self.user} - {self.user.last_name} {self.user.first_name}'

    def get_image_x300(self):
        return get_thumbnail(
            self.image,
            '300x300',
            quality=51,
            crop='center',
        )

    def image_tmb(self):
        if self.image:
            return mark_safe(
                f'<img scr="{self.image.url}" width=50px>',
            )

        return 'Нет изображения'

    image_tmb.short_description = 'превью'
    image_tmb.allow_tags = True

    list_display = ['image_tmb']

    class Meta:
        verbose_name = 'Данные пользователя'
        verbose_name_plural = 'Данные пользователей'
        db_table = 'users_profiles'
