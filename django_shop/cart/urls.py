from django.urls import path
from .views import CartListView, OrdersListView, remove_from_cart, add_to_cart, increment, decrement, make_order

urlpatterns = [
    path('increment/', increment, name='increment'),
    path('decrement/', decrement, name='decrement'),

    path('remove/', remove_from_cart, name='remove_from_cart'),
    path('add/', add_to_cart, name='add_to_cart'),

    path('order/', make_order, name='make_order'),

    path('orders/', OrdersListView.as_view(), name='orders'),
    path('', CartListView.as_view(), name='cart'),
]
