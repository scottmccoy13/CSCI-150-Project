from .models import Asset
from django.shortcuts import render, get_object_or_404
from django.views import generic

def assetHome(request):
	allAssets = Asset.objects.all()
	#return render(request, 'assetdata/index.html', {'allAssets': allAssets})
	#selectedAsset = Asset.objects.all()
	return render(request, 'assetdata/index.html', {'allAssets': allAssets})

def assetDetail(request, asset_id):
	#trys to get asset id, if doesnt exist then throws 404
	asset = get_object_or_404(Asset, pk=asset_id)
	return render(request, 'assetdata/detail.html', {'asset': asset, 'asset_id': asset.id})

def onRent(request, asset_id):
	asset = get_object_or_404(Asset, pk=asset_id)

	try:
		allAssets = Asset.objects.all()
		
	except (KeyError, Asset.DoesNotExist):
		return render(request, 'AssetData/detail.html', {
			'asset':asset,
			'error_message': "You did not select a valid asset"
			})
	else:
		asset.availibility = not(asset.availibility) 
		asset.save()
		return render(request, 'assetdata/detail.html', {'allAsset': allAssets, 'asset_id': asset.id, 'asset': asset})
		