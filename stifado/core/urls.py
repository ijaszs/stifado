
from django.urls import path,include
from django.contrib.auth import views as authViews
from . import views
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns = [
        path('', views.index, name='index'),
        path('signup/',views.signup,name='signup'),
        path('login/',views.login,name='login'),
        path('cart/',views.cart,name='cart'),
        path('prodect_list/',views.prodect_list,name='prodectlist'),
        path('checkout/',views.checkout,name="checkout"),






]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


