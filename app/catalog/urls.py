from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.magazine_catalog, name='magazine_catalog'),
]
