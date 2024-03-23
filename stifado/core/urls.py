
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('register_user/',views.register_user,name='register'),
        path('log_in/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
        path('cart/',views.cart,name='cart'),
        path('prodect_list/',views.prodect_list,name='prodectlist'),







]


