from django.urls import path
from . import views

urlpatterns = [
    path('', views.magazine_home, name='magazine_home'),
    path('create', views.news_create, name='news_create'),
]
