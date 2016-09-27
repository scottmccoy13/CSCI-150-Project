from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
class Customer(models.Model):
	first_name = models.CharField(max_length = 250)
	last_name = models.CharField(max_length = 250)
	
	#> python manage.py shell
	#> from CustomerData.models import Customer
	#> Customer.objects.all()
			#for an example test, I added a Customer with first_name = Customer_fname and last_name = Customer_lname
	#output should be: 
	#<QuerySet [<Customer: Customer_fname Customer_lname>]>
	
	def get_absolute_url(self):
		return reverse('CustomerData:index')
		
	def __str__(self):
		return self.first_name + " " + self.last_name
