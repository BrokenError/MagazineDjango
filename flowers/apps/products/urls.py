from django.urls import path, include
from apps.user.views import LoginUser

from . import views

urlpatterns = [
    path('', LoginUser.as_view(), name='magazine_home'),
    path('aboutus/', views.about_us, name='about'),
    path('catalog/', include('apps.catalog.urls')),
    path('cart/', include('apps.cart.urls')),
    path('user/', include('apps.user.urls')),
]
