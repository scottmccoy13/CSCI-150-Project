from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django import forms
from .models import Customer

def index(request):
	return render(request, 'CustomerData/index.html')
	
class CustomerCreate(CreateView):
	model = Customer
	fields = ['first_name', 'last_name']

class DetailView(generic.DetailView):
	model = Customer
	template_name = 'CustomerData/detail.html'
		
class CustomerList(generic.ListView):
		template_name = 'customer_list.html'
		
		def get_queryset(self):
			return Customer.objects.all()

class CustomerDelete(DeleteView):
		model = Customer
		success_url = reverse_lazy('CustomerData:customer_list')

class CustomerSearchForm(forms.Form):
	search = forms.CharField(max_length = 500)

def CustomerSearch(request):
	search_list = Customer.objects.all()
	context = {
				"search_list" : search_list
	}
	if request.method == 'POST':
		form = CustomerSearchForm(request.POST)
		if form.is_valid():
			search = form.cleaned_data['search']
			search_list = Customer.objects.filter(first_name__icontains = search)	
			context = {
				"search_list" : search_list
			}
			return render(request,'CustomerData/search_results.html', context)
	else:
		form = CustomerSearchForm()
	
	return render(request, 'CustomerData/search_for_customer.html', {'form':form}, context)

def CustomerResults(request):
	return render(request, 'search_results.html')
