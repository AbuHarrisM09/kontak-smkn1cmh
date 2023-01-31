from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin



def signin(request):
    return render(request,'sign-in.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def login_view(request): 
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get['username']
            password = form.cleaned_data.get['password']
            user = authenticate(username = username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard/')

        else:
            form = AuthenticationForm()
        return render(request, login.html, {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')

class ProtectedView(LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'next'

