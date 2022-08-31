from .models import Cart, ProductInCart, Order, ProductInOrder
from shop.models import Product


def get_cart(user):
    if user.is_authenticated:
        products = ProductInCart.objects.filter(cart__user=user)
        cart = {}
        for product in products:
            cart[product.id] = product
        return cart
    return False


def get_orders(user):
    if user.is_authenticated:
        view_orders = {}
        orders = Order.objects.filter(customer=user)
        
        for order in orders:
            products =  ProductInOrder.objects.filter(order=order)
            cost = 0
            for product in products: cost += product.product.price * product.quantity
            view_orders[order.id] = {
                    "created" : order.created,
                    "cost": cost,
                    "products" : products
                }
        return view_orders
    return False


def _get_product_in_cart(ProductInCart_id):
    return ProductInCart.objects.get(id=ProductInCart_id)


def increment_product(ProductInCart_id):
    product = _get_product_in_cart(ProductInCart_id)
    product += 1


def decrement_product(ProductInCart_id):
    product = _get_product_in_cart(ProductInCart_id)
    if product > 1:
        product -= 1


def remove_product_from_cart(ProductInCart_id):
    product = _get_product_in_cart(ProductInCart_id)
    product.delete()


def add_product_to_cart(user, product_id):
    cart = Cart.objects.get(user=user)
    product = Product.objects.get(id=product_id)
    if product in cart.products.all():
        ProductInCart_id = ProductInCart.objects.get(cart=cart, product__id=product_id)
        increment_product(ProductInCart_id.id)
    else:
        cart.products.add(product, through_defaults={'quantity': 1})


def create_order(user, id_products_in_cart):
    products = ProductInCart.objects.filter(id__in=id_products_in_cart)
    order = Order.objects.create(customer=user)
    for in_order in products:
        order.products.add(in_order.product, through_defaults={'quantity': in_order.quantity})
        in_order.delete()

