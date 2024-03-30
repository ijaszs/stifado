from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_user, name='register'),
    path('cart/', views.cart, name='cart'),
    path('restaurants/<int:id>/products/',views.product_list, name='product_list'),
    path('log_in/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    # Add other URL patterns as needed
]

