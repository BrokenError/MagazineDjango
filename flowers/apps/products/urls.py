from django.urls import path, include
from .views import *

urlpatterns = [
    path('', SignupLoginView.as_view(), name='magazine_home'),
    path('catalog/', include('apps.catalog.urls')),
    path('cart/', include('apps.cart.urls')),
    path('user/', include('apps.user.urls')),
]
