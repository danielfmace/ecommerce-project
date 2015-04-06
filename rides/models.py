from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
	user = models.OneToOneField(User)
	has_car = models.BooleanField(default=True)
	seats = models.IntegerField(max_length=2)
	rating = models.FloatField(max_length=1, default=0)
	phone = models.IntegerField(max_length=10)
	def __str__(self):
		return "(" + self.user.first_name + ", " + self.user.last_name + ", " + self.user.email + ")"

class Location(models.Model):
	name = models.CharField(max_length=200, default="Name")
	lat = models.IntegerField(default=0)
	lon = models.IntegerField(default=0)
	def __str__(self):              
		return "(" + self.name + "," + self.lat + ", " + self.lon + ")"

class Start(models.Model):
	name = models.CharField(max_length=200)
	location = models.OneToOneField(Location)

class Dest(models.Model):
	name = models.CharField(max_length=200)
	location = models.OneToOneField(Location)

class Ride(models.Model):
	driver = models.OneToOneField(User)
	seats = models.IntegerField(max_length=2)
	taken = models.IntegerField(max_length=2)
	dest = models.OneToOneField(Dest)
	start = models.OneToOneField(Start)
	riders = models.ManyToManyField(Student)





