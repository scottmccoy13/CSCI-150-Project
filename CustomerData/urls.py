from django.conf.urls import url
from. import views

app_name = 'CustomerData'

urlpatterns = [
	
	#/CustomerData/
	url(r'^$', views.index, name = 'index'),
	
]