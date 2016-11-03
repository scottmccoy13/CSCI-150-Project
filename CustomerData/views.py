from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django import forms
from .models import Customer

def index(request):
	search_list = Customer.objects.all()
	list = search_list
	temp = {}
	search_list2 = {}
	search_list3 = {}
	search_list4 = {}	
	search_form = CustomerSearchForm()
	add_form = AddCustomerForm()
	
	if request.method == 'POST':
		#search for customer
		if 'search_form' in request.POST:
			search_form = CustomerSearchForm(request.POST)
			if search_form.is_valid():
				search = search_form.cleaned_data['search']
				split_search = search.split()
				count = 0
				search = {}
				
				for x in split_search[:2]:
					search[count] = x
					count += 1

				search_list = Customer.objects.filter(first_name__icontains = search[0])
				temp = Customer.objects.exclude(first_name__icontains = search[0])
			
				if len(search) == 2:
					search_list2 = temp.filter(last_name__icontains = search[1])
					temp = temp.exclude(last_name__icontains = search[1])
					search_list3 = temp.filter(first_name__icontains = search[1])
					temp = temp.exclude(first_name__icontains = search[1])
					search_list4 = temp.filter(last_name__icontains = search[0])
				else: 
					search_list2 = temp.filter(last_name__icontains = search[0])
	
			context = {
				"search_list" : search_list, 
				"search_list2" : search_list2,				
				"search_list3" : search_list3,
				"search_list4" : search_list4,
				"search_form": search_form,
				"add_form": add_form
			}	
			return render(request, 'CustomerData/index.html', context)
		
		#add customer
		elif 'add_form' in request.POST:
			add_form = AddCustomerForm(request.POST)
			if add_form.is_valid():
				first = add_form.cleaned_data['first_name']
				last = add_form.cleaned_data['last_name']
				new_customer = Customer.objects.create(first_name = first, last_name = last,)
				new_customer.save()
				
				context = {
					"add_form": AddCustomerForm(),
					"search_form": search_form, 
					"list": list
				}
				
				return render(request, 'CustomerData/index.html', context)
			else:
				context = {
					"add_form": add_form,
					"search_form": search_form, 
					"list": list
				}
				return render(request, 'CustomerData/index.html', context)
		
		elif 'remove_button' in request.POST:
			deletelist = request.POST.getlist('items[]') 
		
			for k in deletelist:
				Customer.objects.filter(id = k).delete()
				
			list = Customer.objects.all()
			
			context = {
				"add_form": add_form,
				"search_form": search_form, 				
				"list": list,
			}
			
			return render(request, 'CustomerData/index.html', context)
				
	else: #if request.method == 'GET'
		context = {
			"add_form": add_form,
			"search_form": search_form, 				
			"list": list
		}
		return render(request, 'CustomerData/index.html', context)
		
class CustomerSearchForm(forms.Form):
	search = forms.CharField(max_length = 500, label="")
	
class AddCustomerForm(forms.Form):
	first_name = forms.CharField(max_length = 250)
	last_name = forms.CharField(max_length = 250)

class DetailView(generic.DetailView):
	model = Customer
	template_name = 'CustomerData/detail.html'