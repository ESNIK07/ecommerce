from django.urls import path
from .views import lista_productos, detalle_producto
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', lista_productos, name='lista_productos'),
    path('producto/<int:producto_id>/', detalle_producto, name='detalle_producto'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)