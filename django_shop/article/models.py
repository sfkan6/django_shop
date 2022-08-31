from django.db import models

from shop.models import Product

# Create your models here.


class Article(models.Model):
    name = models.CharField(max_length=150, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Основной текст')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата Создания')
    products = models.ManyToManyField(Product, blank=True, verbose_name='Товары')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.name

