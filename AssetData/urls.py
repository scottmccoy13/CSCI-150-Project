from django.conf.urls import url

from AssetData import views

urlpatterns = [
    url(r'^$', views.assetHome), # /assetdata/
    url(r'^(?P<asset_id>[0-9]+)/$', views.assetDetail, name='assetDetail'), #
]
