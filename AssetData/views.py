from django.http import HttpResponse
from .models import Asset

def assetHome(request):
    return HttpResponse("<h1>Asset Data</h1>") 
	
def assetDetail(request, asset_id):
	return HttpResponse("<h2>Details for asset ID:" + str(asset_id) + "</h2>")