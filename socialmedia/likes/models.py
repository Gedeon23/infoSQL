from django.db import models
from posts.models import Post
from django.contrib.auth.models import User

# Create your models here.
class Like(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, related_name='post', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)