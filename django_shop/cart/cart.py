from django.conf import settings
from shop.models import Product


class AnonCart(object):
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def remove(self, product_id):
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def add(self, product_id, quantity=1):
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0}

        self.cart[product_id]['quantity'] += quantity
        self.save()

    def steal(self, product_id, quantity=1):
        if product_id in self.cart:
            if self.cart[product_id]['quantity'] > 1:
                self.cart[product_id]['quantity'] -= quantity
            else:
                del self.cart[product_id]

            self.save()

    def get_products(self):
        cart = {}
        if self.cart.keys():
            for product_id in self.cart.keys():
                product = Product.objects.get(id=product_id)
                product.quantity = self.cart[product_id]['quantity']
                cart[product_id] = {
                    'id': product_id,
                    'product': product,
                    'quantity': self.cart[product_id]['quantity'],
                }
        return cart

    def __len__(self):
        return len(self.cart.values())



