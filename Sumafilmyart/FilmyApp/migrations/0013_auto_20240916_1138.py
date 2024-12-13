# Generated by Django 3.2.6 on 2024-09-16 06:08

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FilmyApp', '0012_carrers_alter_application_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('Body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('primary_image', models.ImageField(upload_to='uploads/')),
                ('seondary_image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('optional_image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('date_published', models.DateField()),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('author', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='application',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 16, 11, 38, 24, 547573)),
        ),
        migrations.AlterField(
            model_name='collaboration',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 16, 11, 38, 24, 547573)),
        ),
        migrations.AlterField(
            model_name='contactdata',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 16, 11, 38, 24, 547573)),
        ),
        migrations.AlterField(
            model_name='ideas',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 16, 11, 38, 24, 547573)),
        ),
        migrations.AlterField(
            model_name='sponsorship',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 16, 11, 38, 24, 547573)),
        ),
    ]