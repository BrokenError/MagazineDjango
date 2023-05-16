from django.urls import path

from . import views

urlpatterns = [
    path('', views.magazine_catalog, name='magazine_catalog'),
    path('events', views.catalog_events, name='События'),
    path('bouquets', views.catalog_bouquets, name='Букеты'),
    path('stuffed-toys', views.catalog_stuffed_toys, name='Мягкие игрушки'),
    path('decor', views.catalog_decor, name='Декор'),
    path('other', views.catalog_other, name='Другое'),
    path('magazine_search/', views.magazine_search, name='magazine_search')
]
