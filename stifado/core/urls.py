from django.urls import path
from .views.user_views import register_user
from .views.product_views import product_list, cart
from .views.general_views import index
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', index, name='index'),
    path('register/', register_user, name='register'),
    path('cart/', cart, name='cart'),
    path('products/',product_list, name='product_list'),
    path('log_in/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    # Add other URL patterns as needed
]


