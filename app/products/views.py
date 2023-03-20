from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.views import LoginView

from .models import *
from .forms import *

def magazine_home(request):
    return render(request, 'products/main.html')


def user_basket(request):
    return render(request, 'products/basket.html')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'products/main.html'

    def get_success_url(self):
        return reverse_lazy('magazine_home')
# Create your views here.
