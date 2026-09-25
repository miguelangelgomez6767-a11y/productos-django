from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm


def lista_productos(request):
    productos = Producto.objects.all().order_by('id')

    return render(
        request,
        'lista_productos.html',
        {'productos': productos}
    )


def nuevo_producto(request):

    if request.method == 'POST':
        formulario = ProductoForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('lista_productos')

    else:
        formulario = ProductoForm()

    return render(
        request,
        'nuevo_producto.html',
        {'formulario': formulario}
    )