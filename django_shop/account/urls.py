from django.urls import path
from . import views


urlpatterns = [
    path('', views.auth, name='auth'),
    path('signup/', views.signup, name='signup'),
    path('<int:pk>/', views.Profile.as_view(), name='profile'),
    path('logout/', views.log_out, name='logout'),
]