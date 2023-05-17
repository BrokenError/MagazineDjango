from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from apps.cart.forms import CartAddProductForm
from apps.products.forms import LoginUserForm
from .models import Categories, Products

context = {
    'form': LoginUserForm,
    'count': 0,
    'cat': Categories.objects.order_by('date'),
    'cart_product_form': CartAddProductForm(),
}


# TODO duplicate code
def magazine_catalog(request):
    context['cat_selected'] = 'Каталог'
    prod = Products.objects.order_by('date_created')
    paginator = Paginator(prod, 21)
    page_number = request.GET.get('page', 1)
    context['prod'] = prod
    context['posts'] = paginator.page(page_number)
    return render(request, 'catalog/catalog.html', context=context)


def catalog_events(request):
    context['cat_selected'] = 'События'
    context['prod'] = Products.objects.filter(cat_id=1)
    return render(request, 'catalog/catalog.html', context=context)


def catalog_bouquets(request):
    context['cat_selected'] = 'Букеты'
    context['prod'] = Products.objects.filter(cat_id=2)
    return render(request, 'catalog/catalog.html', context=context)


def catalog_stuffed_toys(request):
    context['cat_selected'] = 'Мягкие игрушки'
    context['prod'] = Products.objects.filter(cat_id=3)
    return render(request, 'catalog/catalog.html', context=context)


def catalog_decor(request):
    context['cat_selected'] = 'Декор'
    context['prod'] = Products.objects.filter(cat_id=4)
    return render(request, 'catalog/catalog.html', context=context)


def catalog_other(request):
    context['cat_selected'] = 'Другое'
    context['prod'] = Products.objects.filter(cat_id=5)
    return render(request, 'catalog/catalog.html', context=context)


def product_detail(request, prod_id, slug):
    product = get_object_or_404(Products, id=prod_id, slug=slug)
    cart_product_form = CartAddProductForm()
    return render(request, 'cart/detail.html', {'product': product,
                                                'cart_product_form': cart_product_form})


def magazine_search(request):
    return render(request, 'catalog/catalog.html', context=context)
