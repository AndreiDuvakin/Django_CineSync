# Generated by Django 4.2 on 2024-04-26 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_initial_squashed_0007_alter_order_datetime_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='ticket',
            options={'verbose_name': 'билет', 'verbose_name_plural': 'Билеты'},
        ),
    ]
