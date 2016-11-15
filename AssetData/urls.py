from django.conf.urls import url
from . import views
from AssetData import views
from django.views.generic import TemplateView

app_name = 'AssetData'

urlpatterns = [
    url(r'^$', views.assetHome, name='assetHome'), # /assetdata/
    url(r'^(?P<asset_id>[0-9]+)/$', views.assetDetail, name='assetDetail'), # /assetdata/#/
    # for changing rent status
    url(r'^(?P<asset_id>[0-9]+)/availibility/$', views.onRent, name='availibility'),

]
