# Generated by Django 5.0.3 on 2024-04-06 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='direction',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='vacancy',
            options={'ordering': ['-pk']},
        ),
    ]
