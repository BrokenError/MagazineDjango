from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    # path('', views.magazine_home, name='magazine_home'),
    path('', LoginUser.as_view(), name='magazine_home'),
    path('catalog/', include('catalog.urls')),
    path('basket', views.user_basket, name='user_basket'),
    path('user/', include('user.urls')),
    # path('', include('user.urls'), name='user_basket'),
]
