from django.shortcuts import render
from .models import Categories


def magazine_catalog(request):
    # cat = 
    return render(request, 'catalog/catalog.html')
