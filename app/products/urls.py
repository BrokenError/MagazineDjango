from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.magazine_home, name='magazine_home'),
    path('catalog/', include('catalog.urls')),
    path('basket', views.user_basket, name='user_basket'),
    path('login', views.user_login, name='user_login'),
]
