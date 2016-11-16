from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from .forms import UserForm
from django.shortcuts import reverse,HttpResponseRedirect

def index(request):
    return render(request,'login/login.html')

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'login/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('calendar'))
            else:
                return render(request, 'login/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login/login.html', {'error_message': 'Invalid login'})
    return render(request, 'login/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('calendar'))
    context = {
        "form": form,
    }
    return render(request, 'login/regf.html', context)
