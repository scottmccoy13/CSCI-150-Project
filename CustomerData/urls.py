from django.conf.urls import url
from django.views.generic import TemplateView

from. import views

app_name = 'CustomerData'

urlpatterns = [
	
	#/CustomerData/
	url(r'^$', views.index, name = 'index'),
	url(r'(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'detail'),
	url(r'^remove/(?P<pk>\d+)$', views.CustomerDelete.as_view(), name = 'remove_customer'),
]