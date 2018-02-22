from django.http import HttpResponse
from django import forms
from django.template import loader
from django.shortcuts import render, redirect
from designer.admin import UserCreationForm
from django.contrib.auth import login, authenticate, logout


def index(request):
  return render(request, 'index.html',)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index.html')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/login')
    else:
        return redirect('/index')
    
    
    
