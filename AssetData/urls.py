from django.conf.urls import url

from AssetData import views

urlpatterns = [
    url(r'^$', views.dummy)
]
