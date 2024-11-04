from django.db import models

# Create your models here.
class Album(models.Model):
 name = models.CharField(max_length=100)
 artist = models.ForeignKey(Artists) # creates a foreign key to the 'Artists' table
 release_date = models.DateField()
 # Add more fields as needed