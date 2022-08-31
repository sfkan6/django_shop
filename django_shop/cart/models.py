from django.db import models
from account.models import User
from shop.models import Product

# Create your models here.


class Cart(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE, verbose_name='Пользователь')
    products = models.ManyToManyField(Product, verbose_name='Товары', blank=True, through='ProductInCart')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'

    def __str__(self):
        return f'Корзина {self.user}'


class ProductInCart(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='Корзина')
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE, related_name='product_in_cart')
    quantity = models.PositiveSmallIntegerField(verbose_name='Количество')

    def __add__(self, other):
        self.quantity += other
        self.save()

    def __sub__(self, other):
        self.quantity -= other
        self.save()

    def __gt__(self, other):
        return self.quantity > other


class Order(models.Model):
    customer = models.ForeignKey(User, related_name='customer',
                                 on_delete=models.CASCADE, verbose_name='Покупатель')
    products = models.ManyToManyField(Product, verbose_name='Товары', blank=True, through='ProductInOrder')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата и Время создание')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-created']

    def __str__(self):
        return f'{self.customer} - {self.created}'


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE, related_name='product_in_order')
    quantity = models.PositiveSmallIntegerField(verbose_name='Количество')
