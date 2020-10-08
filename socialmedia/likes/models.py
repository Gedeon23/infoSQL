from django.db import models
from posts.models import Post
from django.contrib.auth.models import User

# Create your models here.
class Like(models.Model):
    ''' like  post '''

    post = models.OneToOneField(Post, related_name="likes", on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='requirement_comment_likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.post.content)[:30]

class DisLike(models.Model):
    ''' Dislike  post '''

    post = models.OneToOneField(User, related_name="dis_likes", on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='requirement_comment_dis_likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.post.content)[:30]