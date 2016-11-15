from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
class Customer(models.Model):
	first_name = models.CharField(max_length = 250)
	last_name = models.CharField(max_length = 250)
	
	#gives a string version of class object 
	def __str__(self):
		return self.first_name + " " + self.last_name
