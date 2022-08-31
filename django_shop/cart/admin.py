from django.contrib import admin
from .models import Cart, ProductInCart, Order, ProductInOrder

# Register your models here.


class ProductsInCartInLine(admin.TabularInline):
    model = ProductInCart

    verbose_name = 'Товар в корзине'
    verbose_name_plural = 'Товары в корзине'


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user',)

    inlines = (ProductsInCartInLine, )


class ProductsInOrderInLine(admin.TabularInline):
    model = ProductInOrder

    verbose_name = 'Товар в Заказе'
    verbose_name_plural = 'Товары в Заказе'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'created',)
    ordering = ('created',)

    inlines = (ProductsInOrderInLine,)
