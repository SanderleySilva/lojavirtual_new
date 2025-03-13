from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loja_app.urls')),
    path('usuarios/', include('usuarios_app.urls')),
    path('carrinho/', include(('carrinho_app.urls', 'carrinho_app'), namespace='carrinho_app')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
