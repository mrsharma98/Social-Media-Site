from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms
# Create your views here.

class SignUp(CreateView):

    form_class = forms.UserCreateForm
    # just equating the form_class with UserCreateForm we created
    success_url = reverse_lazy('login')
    # if user successfully signed up then they will redirect to the login page
    template_name = 'accounts/signup.html'
    # template is where the user will fill the signup form
