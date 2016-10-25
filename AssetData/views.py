from django.http import HttpResponse
from .models import Asset
from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django import forms


def assetHome(request):
    return HttpResponse("<h1>Asset Data</h1>") 
	
def assetDetail(request, asset_id):
	return HttpResponse("<h2>Details for asset ID:" + str(asset_id) + "</h2>")

class assetCreate(CreateView):
	model = Asset 
	fields = ['cost', 'name', 'availability', 'outLength', 'currOwn']
	
