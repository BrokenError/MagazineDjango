from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.user_info, name='user'),
    path('login', views.user_login, name='login'),
]
