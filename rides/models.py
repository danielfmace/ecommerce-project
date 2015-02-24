from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	phone = models.IntegerField(max_length=10)
	def __str__(self):
		return "(" + self.name + ", " + self.email + ")"


class Location(models.Model):
	lat = models.IntegerField(default=0)
	lon = models.IntegerField(default=0)
	def __str__(self):              
		return "(" + self.lat + ", " + self.lon + ")"


class University(models.Model):
	location = models.ForeignKey(Location)
	name = models.CharField(max_length=200)
	def __str__(self):              
		return self.name

