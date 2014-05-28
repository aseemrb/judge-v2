from django.db import models

# Create your models here.
class Problems(models.Model):
	problem_name = models.CharField(max_length=200)
	problem_statement = models.TextField()
	input = models.TextField()
	solvedby = models.IntegerField(default=0)
	output = models.TextField()
	points = models.IntegerField()
	time = models.IntegerField()

class Users(models.Model):
	username = models.CharField(max_length=50)
	status = models.IntegerField(max_length=20, default=0)
	solved = models.IntegerField(max_length=20, default=0)
	score = models.FloatField(default=0)
	posts = models.IntegerField(max_length=20, default=0)

class Solve(models.Model):
	problem_id = models.IntegerField()
	username = models.CharField(max_length=50)
	status = models.IntegerField(default=1)
	attempts = models.IntegerField(default=1)
	score = models.FloatField()
	solution = models.TextField()
	time = models.IntegerField()
	language = models.IntegerField()

class LanguagePreference(models.Model):
	name_of_event = models.CharField(max_length=50)
	start_time = models.CharField(max_length=100)
	end_time = models.CharField(max_length=100)
	c = models.IntegerField(default = 0)
	cpp = models.IntegerField(default = 0)
	java = models.IntegerField(default = 0)
	python = models.IntegerField(default = 0)
	formula = models.CharField(max_length=200)
