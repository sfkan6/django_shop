from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


class Category(MPTTModel):
    name = models.CharField(
        max_length=200,
        verbose_name='Категория',
        unique=True
    )

    slug = models.SlugField(unique=True)

    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='Каталог',
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('-id',)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'shop:category',
            kwargs={'category_slug': self.slug}
        )


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='products',
        verbose_name='Категория'
    )

    title = models.CharField(
        max_length=300,
        verbose_name='Название'
    )

    description = models.TextField(
        max_length=1000,
        verbose_name='Описание'
    )

    image = models.ImageField(
        upload_to='products/',
        verbose_name='Изображение'
    )

    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена', default=0)

    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'shop:product_detail',
            kwargs={
                'category_slug': self.category.slug,
                'product_slug': self.slug,
            }
        )


class Review(models.Model):

    product = models.ForeignKey(
        Product,
        related_name='reviews',
        on_delete=models.PROTECT,
        verbose_name='Товар'
    )

    name = models.CharField(
        max_length=64,
        verbose_name='Имя',
    )

    rating = models.PositiveSmallIntegerField(
        verbose_name='Рейтинг'
    )

    review = models.TextField(
        max_length=255,
        verbose_name='Отзыв'
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.name
