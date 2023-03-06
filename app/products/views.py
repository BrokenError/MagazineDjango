from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView

def magazine_home(request):
    return render(request, 'products/main.html')


def user_basket(request):
    return render(request, 'products/basket.html')


def user_login(request):
    return render(request, 'products/login.html')

# Create your views here.
