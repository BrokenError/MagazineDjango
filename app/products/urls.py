from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', views.Login.as_view(), name='magazine_home'),
    path('catalog/', include('catalog.urls')),
    path('cart/', include('cart.urls')),
    path('user/', include('user.urls')),
]
