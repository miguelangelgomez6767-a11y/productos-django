from django.shortcuts import get_object_or_404, redirect, render

from .forms import CategoriaForm, ProductoForm
from .models import Categoria, Producto


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


def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == 'POST':
        formulario = ProductoForm(request.POST, instance=producto)

        if formulario.is_valid():
            formulario.save()
            return redirect('lista_productos')
    else:
        formulario = ProductoForm(instance=producto)

    return render(
        request,
        'editar_producto.html',
        {
            'formulario': formulario,
            'producto': producto,
        }
    )


def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')

    return render(
        request,
        'eliminar_producto.html',
        {'producto': producto}
    )


def lista_categorias(request):
    categorias = Categoria.objects.all().order_by('id')

    return render(
        request,
        'lista_categorias.html',
        {'categorias': categorias}
    )


def nueva_categoria(request):
    if request.method == 'POST':
        formulario = CategoriaForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('lista_categorias')
    else:
        formulario = CategoriaForm()

    return render(
        request,
        'nueva_categoria.html',
        {'formulario': formulario}
    )


def editar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)

    if request.method == 'POST':
        formulario = CategoriaForm(request.POST, instance=categoria)

        if formulario.is_valid():
            formulario.save()
            return redirect('lista_categorias')
    else:
        formulario = CategoriaForm(instance=categoria)

    return render(
        request,
        'editar_categoria.html',
        {
            'formulario': formulario,
            'categoria': categoria,
        }
    )


def eliminar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)

    if request.method == 'POST':
        categoria.delete()
        return redirect('lista_categorias')

    return render(
        request,
        'eliminar_categoria.html',
        {'categoria': categoria}
    )
