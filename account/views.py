from django.http import HttpResponse
from django import forms
from django.template import loader
from django.shortcuts import render, redirect
from designer.admin import UserCreationForm
from django.contrib.auth import login, authenticate



def index(request):
  # return HttpResponse("Hello world, you have arrived at the index page" )

  return render(request, 'index.html',)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
