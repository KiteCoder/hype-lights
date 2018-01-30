from django.http import HttpResponse
from django import forms
from django.template import loader

def index(request):
  return HttpResponse("Hello world, you have arrived at the login page" )
