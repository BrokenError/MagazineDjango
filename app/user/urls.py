from django.urls import path, include
from . import views
from products.forms import *
from .views import *

urlpatterns = [
    path('', views.user_info, name='user'),
    path('registration/', RegisterUser.as_view(), name='registration'),
    path('logout/', views.logout_user, name='logout'),
]
