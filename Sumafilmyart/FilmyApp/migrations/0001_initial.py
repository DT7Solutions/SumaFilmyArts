# Generated by Django 4.1.2 on 2022-10-29 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone', models.CharField(max_length=10)),
                ('Subject', models.CharField(max_length=100)),
                ('Message', models.CharField(max_length=500)),
            ],
        ),
    ]
