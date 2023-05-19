from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from apps.cart.forms import CartAddProductForm
from apps.products.forms import LoginUserForm
from .models import Categories, Products

context = {
    'form': LoginUserForm,
    'count': 0,
    'cat': Categories.objects.order_by('date'),
    'cart_product_form': CartAddProductForm(),
}


class SearchResultView(ListView):
    model = Products
    template_name = 'catalog/search.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context['title'] = 'Поиск товара'
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is None:
            object_list = Products.objects.all()
        else:
            object_list = Products.objects.filter(Q(title__icontains=query) or Q(slug__icontains=query))
        context['prod'] = object_list
        return context


def magazine_catalog(request):
    context['prod'] = Products.objects.all()
    context['cat_selected'] = 0
    prod = Products.objects.order_by('date_created')
    paginator = Paginator(prod, 21)
    page_number = request.GET.get('page', 1)
    context['prod'] = prod
    context['posts'] = paginator.page(page_number)
    return render(request, 'catalog/catalog.html', context=context)


def show_categories(request, slug):
    cater = get_object_or_404(Categories, slug=slug)
    context['prod'] = Products.objects.filter(cat=cater.id)
    context['cat_selected'] = cater.id
    return render(request, 'catalog/catalog.html', context=context)


def magazine_search(request):
    return render(request, 'catalog/catalog.html', context=context)
