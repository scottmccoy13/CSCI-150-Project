from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django import forms
from .models import Customer

#initial page /CustomerData/ in template "index.html" and values for list, search_form, and add_form 
def index(request):
	#cannot access page if user is not log in
	if not request.user.is_authenticated():
		return render(request, 'login/login.html')
	#intialize variables
	search_list = Customer.objects.all()
	list = search_list
	temp = {}
	search_list2 = {}
	search_list3 = {}
	search_list4 = {}	
	search_form = CustomerSearchForm()
	add_form = AddCustomerForm()
	
	if request.method == 'POST':	
		#if the name of the button is "remove_button" and the method="POST"
		if 'remove_button' in request.POST:
			#return the list of items (checkboxes) that were checked
			deletelist = request.POST.getlist('items[]') 
		
			#for each item in the deletelist, find them and delete them.
			for k in deletelist:
				Customer.objects.filter(id = k).delete()
				
			#give the updated Customer list into variable list
			list = Customer.objects.all()

			#return list with context
			#context is a dictionary that can hold other data that can be return with render()
			#at this time, search_form = CustomerSearchForm() and add_form = AddCustomerForm()
			#need to return them too because, after removing Customer(s), the pages reload and the add_form and search_form must be available
			context = {
				"add_form": add_form,
				"search_form": search_form, 				
				"list": list,
			}
			
			return render(request, 'CustomerData/index.html', context)
				
	else: #if request.method == 'GET'
		#if the name of the button is "search_form" 
		#this search form is case insensitive and only takes in 2 words maximum and 1 character minimum, but inputting 1 letter will return all the Customers with that letter in their name.
		if 'search_form' in request.GET:
			#put the input string in variable search
			search = request.GET.get('search', '')
			
			#if var search only contains spaces 
			#for now just change spaces to '.' since no such name will have a . in it.
			if search.isspace():
				search = '.'
			
			#in case there are more than 2 words in search, split them up and put them inside the list split_search
			split_search = search.split()
			count = 0
			search = {}
				
			#this search only takes in the first 2 words, so the last word is ignore
			#since split_searach may contain more than 2 words, put the first 2 words inside the list search
			for x in split_search[:2]:
				search[count] = x
				count += 1
			
			#at this time (line 14) search_list = Customer.objects.all()
			#now we must filter this search_list to only have Customers with first_name CONTAINING (so does not need to be exact) the 1st word (case-insensitive)
			search_list = Customer.objects.filter(first_name__icontains = search[0])
			
			#set temp (line 16) contain the list that did not make into the previous filter
			#temp will be the next search_list to be search if there is another word in the list search
			temp = Customer.objects.exclude(first_name__icontains = search[0])
			
			#if the list search has 2 words then, must filter temp for the remaining Customers that will contain the 2nd word as their last_name or first_name
			#and lastly, see if the any of the rest of the Customers' last_name contains the 1st word
			if len(search) == 2:
				#search for last_name containing the 2nd word
				search_list2 = temp.filter(last_name__icontains = search[1])
				temp = temp.exclude(last_name__icontains = search[1])
				#search for first name containing the 2nd word
				search_list3 = temp.filter(first_name__icontains = search[1])
				temp = temp.exclude(first_name__icontains = search[1])
				#search for last name containing the 1st word
				#since the very first filter only filter in the case that there is only 1 word
				search_list4 = temp.filter(last_name__icontains = search[0])
			else: 
				#else there is only 1 word in search, then must also
				#search for the rest of the Customers' last_name containing the word
				search_list2 = temp.filter(last_name__icontains = search[0])
				
			#make context carry the filter lists, the search_form, and the add_form
			context = {
				"search_list" : search_list, 
				"search_list2" : search_list2,				
				"search_list3" : search_list3,
				"search_list4" : search_list4,
				"search_form": search_form,
				"add_form": add_form
			}	
			
			#after clicking seach button, filter data and send them back in context to the same page 
			return render(request, 'CustomerData/index.html', context)
		
		#else button name is not "search_form"
		#or this is the first time entering this page
		else:
			#returns the full list of Customer, add_form, and search_form 
			context = {
				"add_form": add_form,
				"search_form": search_form, 				
				"list": list
			}
			return render(request, 'CustomerData/index.html', context)
		
#addCustomer function for returning JsonResponse to ajax
def addCustomer(request):
	#there's only 1 if statement for "POST" since the add Customer form's method is set to "POST"
	#not sure how the request.method can be anything other than "POST" so there is no else statement to cover that
	if request.method == "POST":	
		add_form = AddCustomerForm(request.POST)
		#check if the inputted fields are valid
		#they are valid if there is only 1 word for each field and due to the funciton clean(self) in class AddCustomerForm(forms.Form) at line 156,
		#they are also valid if they only contain letters
		if add_form.is_valid():
			#set variables to the newly cleaned_data of the input fields
			first_name = add_form.cleaned_data['first_name']
			last_name = add_form.cleaned_data['last_name']
			
			#create a new Customer with those submitted input
			new_customer = Customer.objects.create(first_name = first_name, last_name = last_name)
			new_customer.save()
			
			#set the response dictionary with id success
			response = {'success': "none"}
			
			#return the data as json back to ajax, so ajax can trigger the else statement that adding Customer is a success
			return JsonResponse(response)
		else: #else the inputted field(s) are not valid
			#initialize empty response dicitonary in case the upcoming if statement are not trigger
			response = {}
			
			#remove leading whitespaces since django still accepts those with whitespaces in the front, but not those in between 
			f = request.POST['first_name'].lstrip()
			l = request.POST['last_name'].lstrip()
			
			#if first_name is all spaces or if there is a non-letter character (including a space) in the name
			#then set an id "error1" to "letters" in response dictionary
			if all(x.isspace() for x in f) or any(not x.isalpha() for x in f): 
				response['error1'] = "letters"
				
			#if last_name is all spaces or if there is a non-letter character (including a space) in the name
			#then set an id "error2" to "letters" in response dictionary
			if all(x.isspace() for x in l) or any(not x.isalpha() for x in l):
				response['error2'] = "letters"
				
			#return the data as json back to ajax, so ajax can use if statements to print out the error if inputs are not accepted 
			return JsonResponse(response)

#search form 
class CustomerSearchForm(forms.Form):
	search = forms.CharField(max_length = 500, label="")
	
#add customer form 
class AddCustomerForm(forms.Form):
	first_name = forms.CharField(max_length = 250)
	last_name = forms.CharField(max_length = 250)
	
	#when calling add_form.is_valid(), this function will be a part of checking if the form is valid
	def clean(self):
		cleaned_data = super(AddCustomerForm, self).clean()
		first = cleaned_data.get('first_name')
		last = cleaned_data.get('last_name')
		#these won't show since I'm using ajax, they are here just so that the else statement in addCustomer(request) will be trigger if all the characters in the string are not letters.
		if not str(first).isalpha() and not str(last).isalpha():
			raise forms.ValidationError("letters")
		elif not str(first).isalpha():
			raise forms.ValidationError("letters")
		elif not str(last).isalpha():
			raise forms.ValidationError("letters")
		return cleaned_data

#detail view of Customer details
class DetailView(generic.DetailView):
	model = Customer
	template_name = 'CustomerData/detail.html'