from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .cart import AnonCart
from .services import get_cart, get_orders, add_product_to_cart, remove_product_from_cart, decrement_product, increment_product, create_order

# Create your views here.


class CartListView(ListView):
    context_object_name = "cart"
    template_name = 'view_cart.html'

    def get_queryset(self):
        cart = get_cart(self.request.user)
        if not cart:
            cart = AnonCart(self.request).get_products()
        return cart



class OrdersListView(ListView):
    context_object_name = "orders"
    template_name = 'view_orders.html'

    def get_queryset(self):
        orders = get_orders(self.request.user)
        if not orders:
            messages.success(self.request, 'Зарегистрируйтесь')
        return orders


def wrap_check(request, option_one, option_two):
    ProductInCart_id = request.POST.get('product_id')
    if request.user.is_authenticated:
        option_one(ProductInCart_id)
    else:
        option_two(ProductInCart_id)


@require_POST
def add_to_cart(request):
    product_id = request.GET.get('product_id')
    if request.user.is_authenticated:
        add_product_to_cart(request.user, product_id)
    else:
        AnonCart(request).add(product_id)
    messages.success(request, 'Товар добавлен в корзину')
    return redirect(request.GET.get('path'))


@require_POST
def remove_from_cart(request):
    wrap_check(request, remove_product_from_cart, AnonCart(request).remove)
    return redirect('cart')


@require_POST
def decrement(request):
    wrap_check(request, decrement_product, AnonCart(request).steal)
    return redirect('cart')


@require_POST
def increment(request):
    wrap_check(request, increment_product, AnonCart(request).add)
    return redirect('cart')


@require_POST
@login_required(login_url='auth')
def make_order(request):
    id_products_in_cart = tuple(request.GET.get('id_products').split(','))  # id_products_in_cart (1, 2, 3)
    create_order(request.user, id_products_in_cart)
    messages.success(request, 'Заказ принят')
    return redirect('cart')
