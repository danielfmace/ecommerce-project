from django.db import models
from django.contrib.auth.models import User
import datetime

class Student(models.Model):
	user = models.OneToOneField(User)
	has_car = models.BooleanField(default=True)
	seats = models.IntegerField(max_length=2)
	rating = models.FloatField(max_length=1, default=0)
	phone = models.IntegerField(max_length=10)
	avatar = models.ImageField(upload_to='images', blank=True, null=True)
	def __str__(self):
		return "(" + self.user.first_name + ", " + self.user.last_name + ", " + self.user.email + ")"

class Location(models.Model):
	name = models.CharField(max_length=200, default="Name")
	lat = models.FloatField(default=0)
	lon = models.FloatField(default=0)
	def __str__(self):              
		return "(" + self.name + ", " + str(self.lat) + ", " + str(self.lon) + ")"

class Start(models.Model):
	name = models.CharField(max_length=200)
	location = models.OneToOneField(Location)
	def __str__(self):
		return self.name

class Dest(models.Model):
	name = models.CharField(max_length=200)
	location = models.OneToOneField(Location)
	def __str__(self):
		return self.name

class Ride(models.Model):
	driver = models.ForeignKey(User)
	seats = models.IntegerField(max_length=2)
	taken = models.IntegerField(max_length=2, default=0)
	dest = models.ForeignKey(Dest)
	start = models.ForeignKey(Start)
	riders = models.ManyToManyField(Student, blank=True, null=True)
	time = models.DateTimeField(default=datetime.datetime.today)
	def __str__(self):
		return self.driver.first_name + " " + self.driver.last_name + " - " + str(self.time)





