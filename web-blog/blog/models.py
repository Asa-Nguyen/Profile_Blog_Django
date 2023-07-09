from django.db import models

# Create your models here.
class Post(models.Model):
    tittle = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateField(auto_now=True)