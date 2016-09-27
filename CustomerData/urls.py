from django.conf.urls import url
from. import views

app_name = 'CustomerData'

urlpatterns = [
	
	#/CustomerData/
	url(r'^$', views.index, name = 'index'),
	url(r'add/$', views.CustomerCreate.as_view(), name = 'add_customer'),
	url(r'customer_list/$', views.CustomerList.as_view(), name = 'customer_list'),
	url(r'^remove/(?P<pk>\d+)$', views.CustomerDelete.as_view(), name = 'remove_customer'),
	url(r'search_for_customer/$', views.CustomerSearch, name = 'search_for_customer'),
]