from django.urls import path
from .views import ProductListView, ProductDetailView

app_name = 'shop'

urlpatterns = [
    path('<str:category_slug>/', ProductListView.as_view(), name='category'),
    path('<str:category_slug>/<slug:product_slug>/', ProductDetailView.as_view(), name='product_detail'),
]