from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title       = models.CharField(max_length=100)
    content     = models.TextField()
    image       = models.ImageField(blank=True, null=True, upload_to="posts/")
    author      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date        = models.DateTimeField(auto_now_add=True)
    is_edited   = models.BooleanField(default=False)
    like_count  = models.IntegerField(default=0)

    def get_total_likes(self):
        return self.likes.users.count()

    def get_total_dis_likes(self):
        return self.dis_likes.users.count()

    def __self__(self):
        return str(self.content)[:30]