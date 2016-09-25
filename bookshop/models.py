from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Book(models.Model):
	name=models.CharField(max_length=100)
	author=models.CharField(max_length=100)
	cover=models.CharField(max_length=7, choices=(("Мягкий","Мягкий"), ("Жесткий","Жесткий")))
	number=models.IntegerField()
	img=models.ImageField(upload_to="bookshop/static/")
	desc=models.TextField()

	def __str__(self):
		return self.name
class Book_User(models.Model):
	user=models.CharField(max_length=200)
	book=models.IntegerField()