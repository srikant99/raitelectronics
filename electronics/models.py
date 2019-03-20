from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
