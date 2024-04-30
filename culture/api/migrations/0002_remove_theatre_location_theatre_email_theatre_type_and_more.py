# Generated by Django 4.2.11 on 2024-04-30 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theatre',
            name='location',
        ),
        migrations.AddField(
            model_name='theatre',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AddField(
            model_name='theatre',
            name='type',
            field=models.CharField(default='noncommercial', max_length=250),
        ),
        migrations.AlterField(
            model_name='theatre',
            name='inn',
            field=models.CharField(max_length=12),
        ),
    ]