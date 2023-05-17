from django.urls import path, include
from apps.user.views import RegisterUser, LoginUser
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', LoginUser.as_view(), name='magazine_home'),
    path('catalog/', include('apps.catalog.urls')),
    path('cart/', include('apps.cart.urls')),
    path('user/', include('apps.user.urls')),
]
