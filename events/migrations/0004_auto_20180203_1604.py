# Generated by Django 2.0.2 on 2018-02-04 00:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='event time'),
        ),
    ]
