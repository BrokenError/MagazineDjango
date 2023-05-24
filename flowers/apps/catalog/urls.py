from django.urls import path

from . import views

urlpatterns = [
    path('', views.magazine_catalog, name='magazine_catalog'),
    path('search/', views.SearchResultView.as_view(), name='search'),
    path('<slug:slug>/', views.show_categories, name='category'),
]
