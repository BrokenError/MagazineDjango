from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

app_name = 'main_app'

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('cart/', include('apps.cart.urls')),
                  path('', include('apps.products.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
