from .models import Asset
from django.shortcuts import render
from django.views import generic
from django.http import Http404


def assetHome(request):
	allAssets = Asset.objects.all()
	return render(request, 'assetdata/index.html', {'allAssets': allAssets})
	
def assetDetail(request, asset_id):
	try:
		asset = Asset.objects.get(pk=asset_id)
	except Asset.DoesNotExist:
		raise Http404("Asset does not exist")
	return render(request, 'assetdata/detail.html', {'asset': asset})


	
