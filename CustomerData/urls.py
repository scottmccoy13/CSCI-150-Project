from django.conf.urls import url
from django.views.generic import TemplateView

from. import views

app_name = 'CustomerData'

urlpatterns = [
	
	#/CustomerData/
	url(r'^$', views.index, name = 'index'),
	#/CustomerData/1/
	url(r'(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'detail'),
	url(r'^add/$', views.addCustomer),
]