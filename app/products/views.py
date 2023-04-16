from django.shortcuts import render, redirect, HttpResponse
from django.db.models import Q
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.views import LoginView
from .models import *
from .forms import *
from catalog.models import Products

class Login(LoginView):
    form_class = LoginUserForm
    template_name = 'products/main.html'

    
    def get_success_url(self):
        return reverse("magazine_home")


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products_images'] = Products.objects.all()[:8]
        return context



def user_basket(request):
    return render(request, 'products/basket.html')


