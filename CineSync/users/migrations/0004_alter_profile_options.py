# Generated by Django 4.2 on 2024-04-26 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_profile_genres_profile_genres'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={
                'verbose_name': 'данные пользователя',
                'verbose_name_plural': 'Данные пользователей',
            },
        ),
    ]
