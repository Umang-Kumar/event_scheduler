# Generated by Django 4.2.4 on 2023-08-31 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventcreation',
            options={'ordering': ['id'], 'verbose_name': 'Event Creation', 'verbose_name_plural': 'Event Creations'},
        ),
        migrations.RemoveField(
            model_name='eventcreation',
            name='start_time',
        ),
        migrations.AddField(
            model_name='eventcreation',
            name='prefered_date_time',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
