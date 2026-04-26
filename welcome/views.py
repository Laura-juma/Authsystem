from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

# Create your views here.
class SignUpView(CreateView):
  form_class=UserCreationForm
  template_name='welcome/register.html'
  success_url=reverse_lazy('login')

class CustomLoginView(LoginView):
  template_name='welcome/login.html'

def login_success(request):
  return render(request, 'welcome/login_success.html')


