from django.db import models
from django.contrib.auth.models import User
import datetime as dt

# Create your models here.
class Tracker(models.Model):
  url = models.URLField()
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tracker', null= True)
  time = models.DateTimeField(auto_now_add=True, null=True)

  def __str__(self):
    return str(self.user.username)

  def save_search(self):
    self.save()