# Generated by Django 5.0.3 on 2024-03-31 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_car_color_alter_car_make'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='number',
            field=models.IntegerField(help_text='Номер Машины'),
        ),
    ]