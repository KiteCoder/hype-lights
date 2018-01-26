from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django import forms
from account.models import User


def process_request(request):

  # process the form
  form = LoginForm()
  if request.method == 'POST':  # just submitted the form
    form = LoginForm(request.POST)
    if form.is_valid():
      # log the user in - connect the user to the request
      #user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
      login(request, form.user)
      #return HttpResponseRedirect('/homepage/index/')
      return HttpResponse('''
        <script>
          window.location.href = '/homepage/index/';
        </script>
      ''')
  
  template_vars = {
    'form': form,
  }
  # return dmp_render(request, 'login.html', template_vars)
  # return django...?
  
  
class LoginForm(forms.Form):
  username = forms.CharField(label='Username', required=True, max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))  
  password = forms.CharField(label='Password', required=True, max_length=100, widget=forms.PasswordInput(attrs={ 'class': 'form-control' }))  

  def clean(self):
    # will not work because password is not plain text in database
    #user = User.objects.get(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
    user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
    if user == None:
      raise forms.ValidationError('The username and password was not found in our system.')
    self.user = user
    return self.cleaned_data