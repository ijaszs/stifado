
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns = [
        path('', views.index, name='index'),
        path('register_user/',views.register_user,name='register'),
        path('login/',views.login_user,name='login'),
        path('log_out/',views.logout_user,name='logout_user'),
        path('cart/',views.cart,name='cart'),
        path('prodect_list/',views.prodect_list,name='prodectlist'),







]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


