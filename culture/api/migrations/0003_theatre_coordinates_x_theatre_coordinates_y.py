# Generated by Django 4.2.11 on 2024-04-30 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_theatre_location_theatre_email_theatre_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='theatre',
            name='coordinates_x',
            field=models.FloatField(default=None),
        ),
        migrations.AddField(
            model_name='theatre',
            name='coordinates_y',
            field=models.FloatField(default=None),
        ),
    ]
