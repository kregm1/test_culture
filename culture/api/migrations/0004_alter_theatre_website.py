# Generated by Django 4.2.11 on 2024-04-30 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_theatre_coordinates_x_theatre_coordinates_y'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theatre',
            name='website',
            field=models.URLField(default=None),
        ),
    ]
