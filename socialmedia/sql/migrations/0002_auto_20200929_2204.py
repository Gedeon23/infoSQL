# Generated by Django 3.1.1 on 2020-09-29 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sql', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Abfrage',
            new_name='Query',
        ),
    ]