from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from users.models import Profile

user = get_user_model()
admin.site.unregister(user)


class ProfileInline(admin.TabularInline):
    can_delete = False
    model = Profile
    fields = [
        Profile.birthday.field.name,
        Profile.image.field.name,
    ]


@admin.register(user)
class UserAdmin(UserAdmin):
    inlines = [
        ProfileInline,
    ]
