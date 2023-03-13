from django.shortcuts import render
from .models import Categories, Products

cat = Categories.objects.order_by('date')
products = Products.objects.order_by('date')

context = {
        'cat': cat,
        'title': 'Категории',
        'prod': products,
        'count': 0,
    }

def magazine_catalog(request):
    # print(context)
    context['cat_selected'] = 'Каталог' 
    return render(request, 'catalog/catalog.html', context=context)


def catalog_events(request):
    context['cat_selected'] = 'События' 
    return render(request, 'catalog/catalog.html', context=context)


def catalog_bouquets(request):
    context['cat_selected'] = 'Букеты' 
    return render(request, 'catalog/catalog.html', context=context)

    
def catalog_stuffed_toys(request):
    context['cat_selected'] = 'Мягкие игрушки' 
    return render(request, 'catalog/catalog.html', context=context)


def catalog_decor(request):
    context['cat_selected'] = 'Декор' 
    return render(request, 'catalog/catalog.html', context=context)


def catalog_other(request):
    context['cat_selected'] = 'Другое' 
    return render(request, 'catalog/catalog.html', context=context)