from django.db import models
from django import forms

# Create your models here.

class Person(models.Model):
	"""
	Model representing a person and their body info
	"""
	
	def __init__(self):
		self.PersonInfo = {}
		self.gender = forms.ChoiceField()
		self.weight = forms.FloatField()
		self.height = forms.IntegerField()
		self.age = forms.IntegerField()
		self.activitylevel = forms.ChoiceField()
		self.restrictions = forms.MultipleChoiceField()
		self.printableGender = "male"
		self.printableActivityLevel = "is sedentary"
		# self.printableHeight = "5ft 0in"

	def __str__(self):
		return self.name

	def get_info(self, field):
		return self.PersonInfo[field]

	def set_printableGender(self):
		if self.gender == "f":
			self.printableGender = "female"

	def set_printableActivityLevel(self):
		if self.activitylevel == 1:
			self.printableActivityLevel = "sedentary"
		if self.activitylevel == 2:
			self.printableActivityLevel = "lightly active"
		if self.activitylevel == 3:
			self.printableActivityLevel = "moderately active"
		if self.activitylevel == 4:
			self.printableActivityLevel = "heavily active"
		if self.activitylevel == 5:
			self.printableActivityLevel = "athlete"

	# def set_printableHeight(self):
	# 	self.printableHeight = str(int(int(self.height) / 12)) + "ft " + str(int(self.height)%12) + "in"

	def update_info(self):
		self.set_printableGender()
		self.set_printableActivityLevel()
		# self.set_printableHeight()
		self.PersonInfo = {"gender": self.gender, "weight": self.weight, "age": self.age, "activitylevel": self.activitylevel, "height": self.height, "restrictions": self.restrictions}