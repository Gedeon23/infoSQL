from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class User_Profile(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, to_field='id')
    profile_pic     = models.ImageField(default='media/profile/blank_profile_picture.png', upload_to='profile/')
    nickname        = models.CharField(max_length=30)
    bio             = models.TextField(blank=True, null=True)