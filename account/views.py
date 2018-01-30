from django.http import HttpResponse
from django import forms
from django.template import loader
from django.shortcuts import render

def index(request):
  # return HttpResponse("Hello world, you have arrived at the index page" )

  return render(request, 'index.html',)
