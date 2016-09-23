from django.http import HttpResponse
from django.shortcuts import render
from .models import Customer

def index(request):
	return render(request, 'index.html')
	