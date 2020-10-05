from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    title       = models.CharField(max_length=100)
    content     = models.TextField()
    author      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date        = models.DateField(auto_now_add=True)