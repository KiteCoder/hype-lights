from django.conf import settings
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from account.models import User




def process_request(request):
  
  # process the form
  form = SignupForm()
  if request.method == 'POST':  # just submitted the form
    form = SignupForm(request.POST)
    if form.is_valid():
      u = User()
      u.username = form.cleaned_data.get('username')
      u.first_name = form.cleaned_data.get('first_name')
      u.last_name = form.cleaned_data.get('last_name')
      u.set_password(form.cleaned_data.get('password'))
      u.address = form.cleaned_data.get('address')
      u.city = form.cleaned_data.get('city')
      u.state = form.cleaned_data.get('state')
      u.zip_code = form.cleaned_data.get('zip_code')
      u.birth_date = form.cleaned_data.get('birth_date')
      u.phone_number = form.cleaned_data.get('phone_number')
      u.save()
      # log the user in
      au = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
      login(request, au)  # must log in with the user retrieved from authenticate
      # redirect to home page
      return HttpResponseRedirect('/homepage/index/')
  
  template_vars = {
    'form': form,
  }
  # return dmp_render(request, 'signup.html', template_vars)
  # figure out hot to render html with normal django
  
class SignupForm(forms.Form):
  username = forms.CharField(label='Username', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  first_name = forms.CharField(label='First Name', required=True, max_length=100, widget=forms.PasswordInput(attrs={ 'class': 'form-control' }))  
  last_name = forms.CharField(label='Last Name', required=True, max_length=100, widget=forms.PasswordInput(attrs={ 'class': 'form-control' }))  
  password = forms.CharField(label='Password', required=True, max_length=100, widget=forms.PasswordInput(attrs={ 'class': 'form-control' }))  
  password2 = forms.CharField(label='Password (again)', required=True, max_length=100, widget=forms.PasswordInput(attrs={ 'class': 'form-control' }))  
  address = forms.CharField(label='Address', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  city = forms.CharField(label='City', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  state = forms.CharField(label='State', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  zip_code = forms.CharField(label='Zip Code', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  birth_date = forms.DateField(label='Birth Date', required=False, input_formats=[ '%Y-%m-%d' ], widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  phone_number = forms.CharField(label='Phone Number', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  

  def clean_username(self):
    username = self.cleaned_data.get('username')
    # check uniqueness of the username
    # method #1 for checking - returns the user OR raises exception
    try:
      user = User.objects.get(username=username)
      raise forms.ValidationError('This username is already taken. Could you already have signed up earlier?')
    except User.DoesNotExist as e:
      pass # this is what we hope for - means unique username
    # method #2 for checking
    users = User.objects.filter(username=username)
    if len(users) > 0:
      raise forms.ValidationError('This username is already taken. Could you already have signed up earlier?')
    # method #3 my favorite
    if User.objects.filter(username=username).count() > 0:
      raise forms.ValidationError('This username is already taken. Could you already have signed up earlier?')
    return username
    

  def clean(self):
    if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
      raise forms.ValidationError('Your passwords need to match.  Please try again.')
    return self.cleaned_data
  