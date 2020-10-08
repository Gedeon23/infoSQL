# Generated by Django 3.1.1 on 2020-10-06 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sql', '0004_query_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='table',
            field=models.CharField(choices=[('auth_user', 'User'), ('likes_table', 'Likes'), ('posts_table', 'Posts'), ('comments_table', 'Comments')], max_length=50),
        ),
    ]