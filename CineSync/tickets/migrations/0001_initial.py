# Generated by Django 4.2 on 2024-04-09 16:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ticket",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "row_number",
                    models.IntegerField(
                        help_text="Номер ряда",
                        validators=[django.core.validators.MinValueValidator(1)],
                        verbose_name="Номер ряда",
                    ),
                ),
                (
                    "column_number",
                    models.IntegerField(
                        help_text="Номер кресла в ряду",
                        validators=[django.core.validators.MinValueValidator(1)],
                        verbose_name="Номер кресла",
                    ),
                ),
            ],
        ),
    ]