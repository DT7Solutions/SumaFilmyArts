# Generated by Django 4.1.2 on 2023-06-02 07:13

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FilmyApp', '0011_remove_application_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=100)),
                ('posted_date', models.DateField(auto_now_add=True)),
                ('description', models.TextField()),
                ('Body', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='application',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 2, 0, 13, 21, 447005)),
        ),
        migrations.AlterField(
            model_name='collaboration',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 2, 0, 13, 21, 447005)),
        ),
        migrations.AlterField(
            model_name='contactdata',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 2, 0, 13, 21, 447005)),
        ),
        migrations.AlterField(
            model_name='ideas',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 2, 0, 13, 21, 447005)),
        ),
        migrations.AlterField(
            model_name='sponsorship',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 2, 0, 13, 21, 447005)),
        ),
    ]
