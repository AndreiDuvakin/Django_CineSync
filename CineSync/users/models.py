import time

from django.conf import settings
from django.db.models import Model, OneToOneField, CASCADE, DateField, CharField, ImageField
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail


class Profile(Model):

    def get_upload_path(self, filename):
        return f'users/avatars/{self.user_id}/{time.time()}_{filename}'

    user = OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name='пользователь',
        related_name='profile',
        related_query_name='profile',
        on_delete=CASCADE,
    )
    birthday = DateField(
        verbose_name='дата рождения пользователя',
        null=True,
        blank=True,
    )
    role = CharField(
        verbose_name='роль пользователя',
        max_length=20,
    )
    image = ImageField(
        null=True,
        blank=True,
        verbose_name="аватар пользователя",
        upload_to=get_upload_path,
    )

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
        verbose_name = 'данные пользователя'
        verbose_name_plural = 'данные пользователей'
        db_table = "users_profiles"
