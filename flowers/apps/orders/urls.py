from django.conf.urls import url

from apps.orders.views import order_create

urlpatterns = [url(r'^create/$', order_create, name='order_create'), ]
