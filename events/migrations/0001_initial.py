# Generated by Django 2.0.2 on 2018-02-04 06:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('description', models.CharField(default='description goes here', max_length=500)),
                ('picture', models.ImageField(default='', upload_to='upload/')),
                ('location', models.CharField(default='location goes here', max_length=100)),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Event time')),
                ('host', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
            ],
        ),
    ]
