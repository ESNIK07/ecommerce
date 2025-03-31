from django.urls import path
from .views import lista_productos, detalle_producto
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', lista_productos, name='lista_productos'),
    path('producto/<int:producto_id>/', detalle_producto, name='detalle_producto'),

    # Rutas para el carrito de compras
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/eliminar/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('carrito/disminuir/<int:producto_id>/', views.disminuir_cantidad, name='disminuir_cantidad'),
    path('carrito/limpiar/', views.limpiar_carrito, name='limpiar_carrito'),
]

# ✅ Se mantiene para servir imágenes en desarrollo
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
