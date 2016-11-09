from __future__ import unicode_literals
from django.db import models
from CustomerData.models import Customer 
from datetime import datetime
#this might let me pull data 
#for customer first and last name, look at foregin key stuff

class Asset(models.Model):
	cost         = models.FloatField()                 #cost of rent for the item
	name         = models.CharField(max_length = 250)  #name of item
	availibility = models.BooleanField(default = True) #if an item is available for rent or not
	outLength    = models.IntegerField(default = 0)    #number of days until item returns
	dateRented   = models.DateField(_("Date"), default=datetime.date.today)
	def __str__(self):
		return self.name                                                   
class currentOwner(models.Model):
	currOwn      = models.ForeignKey(Customer, on_delete=models.CASCADE)                 #current ownership (user foreign key
	#ADD HISTORY PART 

