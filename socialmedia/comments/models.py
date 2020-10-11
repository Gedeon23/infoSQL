from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from posts.models import Post

# Create your models here.
class Comment(models.Model):
    content         = models.TextField()
    post            = models.ForeignKey(Post, on_delete=models.CASCADE)
    author          = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    parent_comment  = models.ForeignKey(to="comments.Comment", on_delete=models.CASCADE, blank=True, null=True)
    date            = models.DateTimeField(auto_now_add=True)
    is_edited       = models.BooleanField(default=False)
    is_pinned       = models.BooleanField(default=False)