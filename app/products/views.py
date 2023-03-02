from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView

def magazine_home(request):
    return render(request, 'products/base.html')


def news_create(request):
    pass

# Create your views here.
