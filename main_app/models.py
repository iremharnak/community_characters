from django.db import models

# Create your models here.
class Character(models.Model):
  name = models.CharField(max_length=100)
  mood = models.CharField(max_length=100)
  quote = models.TextField(max_length=250)

  def __str__(self):
    return self.name