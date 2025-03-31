from django.shortcuts import render, get_object_or_404
from .models import Producto
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .carrito import Carrito

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/lista_productos.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'tienda/detalle_producto.html', {'producto': producto})

def agregar_al_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carrito.agregar(producto)
    return redirect("ver_carrito")

def eliminar_del_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carrito.eliminar(producto)
    return redirect("ver_carrito")

def disminuir_cantidad(request, producto_id):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carrito.disminuir(producto)
    return redirect("ver_carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("ver_carrito")

def ver_carrito(request):
    carrito = Carrito(request)
    return render(request, "tienda/carrito.html", {"carrito": carrito.carrito})
