from http import client
from django.db import models

# Create your models here.
class Project(models.Model):
    nama = models.CharField(max_length=100)
    urls = models.URLField(max_length=600)
    description = models.TextField(max_length=5000)
    category = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    client = models.CharField(max_length=100)
    img_path = models.CharField(max_length=200)
