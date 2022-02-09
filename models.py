from django.db import models
from sqlalchemy import true
#from tables import Description

# Create your models here.

class Meetups(models.Model):
    class Meta: verbose_name_plural = 'Meetups'
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    Description = models.TextField()
