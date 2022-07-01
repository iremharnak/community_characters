from django.db import models

# Create your models here.
class Location(models.Model):
  name = models.CharField(max_length=50)

class Character(models.Model):
  name = models.CharField(max_length=100)
  mood = models.CharField(max_length=100)
  quote = models.TextField(max_length=250)
  locations = models.ManyToManyField(Location)

  def __str__(self):
    return self.name

class Episode(models.Model):
  season = models.CharField(max_length=2)
  episode = models.CharField(max_length=250)


    # Create a character_id FK
  character= models.ForeignKey(Character, on_delete=models.CASCADE)
  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.episode} on {self.season}"