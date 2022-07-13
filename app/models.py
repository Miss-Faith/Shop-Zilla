from django.db import models
import datetime as dt

# Create your models here.
class Tracker(models.Model):
    url = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tracker')
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    return str(self.user.username)

  @classmethod
  def save_post(self):
    self.save()