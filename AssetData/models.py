from __future__ import unicode_literals
from django.db import models

class Asset(models.Model):
	cost         = models.FloatField()                 #cost of rent for the item
	name         = models.CharField(max_length = 250)  #name of item
	availibility = models.BooleanField(default = True) #if an item is available for rent or not
	outLength    = models.IntegerField(default = 0)    #number of days until item returns 
	#ADD HISTORY PART HERE, VIDEO 7
