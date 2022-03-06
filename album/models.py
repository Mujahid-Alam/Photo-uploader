from distutils.command.upload import upload
from pyexpat import model
from django.db import models

# Create your models here.
class Photos(models.Model):
    title = models.CharField(max_length=100)
    images = models.ImageField(upload_to = "images/")
    descriptions = models.CharField(max_length=100)