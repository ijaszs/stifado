from django.urls import path
from core import views
from django.contrib.auth import views as auth_views_core


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_user, name='register'),
    path('cart/', views.cart, name='cart'),
    path('restaurants/<int:id>/products/',views.product_list, name='product_list'),
    path('log_in/', auth_views_core.LoginView.as_view(template_name='login.html'), name='login'),
    path('checkout/', views.checkout, name='checkout'),
    path('search/', views.search_views, name='search'),
    # Add other URL patterns as needed
]


