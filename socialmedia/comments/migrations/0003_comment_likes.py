# Generated by Django 3.1.1 on 2020-10-16 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0007_user_profile_followers'),
        ('comments', '0002_auto_20201016_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(related_name='Comlikes', to='Users.User_Profile'),
        ),
    ]
