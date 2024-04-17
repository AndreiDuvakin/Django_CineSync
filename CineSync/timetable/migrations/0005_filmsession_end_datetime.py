# Generated by Django 4.2 on 2024-04-17 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("timetable", "0004_alter_row_auditorium"),
    ]

    operations = [
        migrations.AddField(
            model_name="filmsession",
            name="end_datetime",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Дата и время начала сеанса"
            ),
        ),
    ]