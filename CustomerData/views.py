from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Customer

def index(request):
	return render(request, 'index.html')
	
class CustomerCreate(CreateView):
		model = Customer
		fields = ['first_name', 'last_name']
		
class CustomerList(generic.ListView):
		template_name = 'customer_list.html'
		
		def get_queryset(self):
			return Customer.objects.all()

class CustomerDelete(DeleteView):
		model = Customer
		success_url = reverse_lazy('CustomerData:customer_list')

def CustomerSearch(request):
	if request.method == "post":
		search = request.POST["search"]
		try:
			#
			return #
		except Customer.DoesNotExist:
			return #
	else:
		return render(request, 'search_for_customer.html')