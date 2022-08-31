from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Category, Product, Review

# Register your models here.


class CustomMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 100


admin.site.register(Category, CustomMPTTModelAdmin)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
    list_filter = ('category',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'rating',)
