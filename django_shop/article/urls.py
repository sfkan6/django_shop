from django.urls import path
from .views import view_home

urlpatterns = [
    path('', view_home, name='home'),
]
