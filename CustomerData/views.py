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
	#assuming searches are only "first_name last_name" 
	#										"last_name first_name"
	#										"first_name"
	#										"last_name"
	
	search_list = Customer.objects.all()
	temp = {}
	search_list2 = {}
	search_list3 = {}
	search_list4 = {}
	
	context = {
				"search_list" : search_list, 
				"search_list2" : search_list2,
				"search_list3" : search_list3,
				"search_list4" : search_list4
	}
	

	if request.method == 'POST':
		form = CustomerSearchForm(request.POST)
		if form.is_valid():
			search = form.cleaned_data['search']
			
			#split search into separate string then add them into one dictionary
			#in case someone searched for "First Last" then search.split() will split it into ["First", "Last"]
			#so they can be search for against first_name and last_name
			split_search = search.split()
			
			#keeps track of how many splits, but max = 2
			count = 0
			#dictionary search
			search = {}
			#put string list split_search's elements into dictionary search
			for x in split_search[:2]:
				search[count] = x
				count += 1
			
			#search_list contains the first_name that contains the first split from search (search first_name = "First")
			search_list = Customer.objects.filter(first_name__icontains = search[0])
			#remove those that are filtered to search_list from temp so won't have duplicates if the other filters are from the same Customer
			#use temp to store those excluded from the previous filter 
			temp = Customer.objects.exclude(first_name__icontains = search[0])
			
			if len(search) == 2:
				#search_list2 containst the last_name that contains the second split from search (search last_name = "Last")
				search_list2 = temp.filter(last_name__icontains = search[1])
				
				temp = temp.exclude(last_name__icontains = search[1])
				
				#if user input "First Last"
				#then now searching for name that might instead be "Last First"
				#searrch_list3 contains the first_name that contains the second split from the search (search first_name = "Last")
				search_list3 = temp.filter(first_name__icontains = search[1])
				
				temp = temp.exclude(first_name__icontains = search[1])
				
				#search_llist4 contains the last_name that contains the second split from the search (search last_name = "First")
				search_list4 = temp.filter(last_name__icontains = search[0])
			else: 
				#if there is only one split (one name that is either first_name or last_name)
				#search_list2 contains the last_name that contains the search
				search_list2 = temp.filter(last_name__icontains = search[0])
				
			#store them into context that holds dictionaries so they can be pass to template
			context = {
				"search_list" : search_list, 
				"search_list2" : search_list2,
				"search_list3" : search_list3,
				"search_list4" : search_list4
			}	
			return render(request,'CustomerData/search_results.html', context)
	else: #if request.method == 'GET'
		form = CustomerSearchForm()
	return render(request, 'CustomerData/search_for_customer.html', {'form':form}, context)

def CustomerResults(request):
	return render(request, 'search_results.html')
