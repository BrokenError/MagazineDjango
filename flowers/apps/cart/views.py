from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import ListView

from apps.cart.cart import Cart
from apps.cart.forms import CartAddProductForm
from apps.catalog.models import Products
from apps.orders.models import Order


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Products, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})


context = {}


class MoreInfo(ListView):
    model = Order
    template_name = 'cart/history-orders.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        orders = Order.objects.filter(user_id=self.request.user.id).order_by('created')
        return {'title': 'История заказов', 'orders': orders}
