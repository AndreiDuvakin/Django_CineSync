# Generated by Django 4.2 on 2024-04-26 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            'timetable',
            '0002_rename_rows_row_filmsession_squashed_0006_remove_auditorium_row_count',
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auditorium',
            options={'verbose_name': 'зал', 'verbose_name_plural': 'Залы'},
        ),
        migrations.AlterModelOptions(
            name='filmsession',
            options={'verbose_name': 'сеанс', 'verbose_name_plural': 'Сеансы'},
        ),
        migrations.AlterModelOptions(
            name='row',
            options={'verbose_name': 'место', 'verbose_name_plural': 'Места'},
        ),
        migrations.AlterField(
            model_name='filmsession',
            name='end_datetime',
            field=models.DateTimeField(
                blank=True,
                null=True,
                verbose_name='Дата и время окончания сеанса',
            ),
        ),
    ]
