# Generated by Django 3.1.1 on 2020-11-17 16:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Users', '0010_auto_20201117_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='followers',
            field=models.ManyToManyField(related_name='is_following', to=settings.AUTH_USER_MODEL),
        ),
    ]
