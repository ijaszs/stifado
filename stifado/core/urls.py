
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns = [
        path('', views.index, name='index'),


        path('login', views.login, name='login'),






]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


