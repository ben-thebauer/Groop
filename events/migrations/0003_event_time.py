# Generated by Django 2.0.2 on 2018-02-03 23:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20180203_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(1998, 1, 30, 0, 0)),
        ),
    ]
