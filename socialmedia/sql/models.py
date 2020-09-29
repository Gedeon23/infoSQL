from django.db import models

# Create your models here
class Query(models.Model):
    title       = models.CharField(max_length=50)
    query       = models.CharField(max_length=250)
    