# Generated by Django 4.1.2 on 2023-01-11 05:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FilmyApp', '0008_collaboration_alter_contactdata_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='collaboration',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 11, 10, 33, 13, 703237)),
        ),
        migrations.AddField(
            model_name='ideas',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 11, 10, 33, 13, 703237)),
        ),
        migrations.AlterField(
            model_name='contactdata',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 11, 10, 33, 13, 703237)),
        ),
    ]