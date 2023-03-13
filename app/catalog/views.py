from django.shortcuts import render
from .models import Categories, Products


context = {
        'count': 0,
        'cat':Categories.objects.order_by('date'),
    }

def magazine_catalog(request):
    context['cat_selected'] = 'Каталог'
    context['prod'] = Products.objects.order_by('date')
    return render(request, 'catalog/catalog.html', context=context)


def catalog_events(request):
    context['cat_selected'] = 'События' 
    context['prod'] = Products.objects.filter(cat_id = 1) 
    return render(request, 'catalog/catalog.html', context=context)


def catalog_bouquets(request):
    context['cat_selected'] = 'Букеты'
    context['prod'] = Products.objects.filter(cat_id = 2)  
    return render(request, 'catalog/catalog.html', context=context)

    
def catalog_stuffed_toys(request):
    context['cat_selected'] = 'Мягкие игрушки'
    context['prod'] = Products.objects.filter(cat_id = 3)  
    return render(request, 'catalog/catalog.html', context=context)


def catalog_decor(request):
    context['cat_selected'] = 'Декор'
    context['prod'] = Products.objects.filter(cat_id = 4)  
    return render(request, 'catalog/catalog.html', context=context)


def catalog_other(request):
    context['cat_selected'] = 'Другое'
    context['prod'] = Products.objects.filter(cat_id = 5)  
    return render(request, 'catalog/catalog.html', context=context)