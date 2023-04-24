from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Short(models.Model):
  initurl = models.CharField(max_length=500)
  shortenurl = models.CharField(max_length=10, default="")
  # make a model so that it acts like a map
  author=models.CharField(max_length=100, default="")

  def __str__(self):
    return f"http://localhost:8000/{self.shortenurl} -> {self.initurl}"