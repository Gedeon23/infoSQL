from django.db import models

# Create your models here
class Query(models.Model):
    my_tables =    (('auth_user', 'User'),
                    ('likes_table', 'Likes'),
                    ('posts_table', 'Posts'),
                    ('comments_table', 'Comments'))
    
    title       = models.CharField(max_length=50)
    table       = models.CharField(max_length=50, choices=my_tables)
    query       = models.CharField(max_length=250)
    