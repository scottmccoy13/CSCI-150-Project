from django.conf.urls import url
from . import views
from AssetData import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.assetHome), # /assetdata/
    url(r'^(?P<asset_id>[0-9]+)/$', views.assetDetail, name='assetDetail'), # /assetdata/#/
   

]
