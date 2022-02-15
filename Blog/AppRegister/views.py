# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from AppRegister.forms import UserRegisterForm

class UserCreateView(CreateView):
    model=User
    success_url = reverse_lazy('login')
    template_name = 'register.html'
    form_class = UserRegisterForm