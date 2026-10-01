# Funciones de Django para buscar objetos, redireccionar y mostrar plantillas.
from django.shortcuts import get_object_or_404, redirect, render

# Importamos los formularios de productos y categorías.
from .forms import CategoriaForm, ProductoForm

# Importamos los modelos de la aplicación.
from .models import Categoria, Producto


# ------------------------------------------------------------
# PRODUCTOS
# ------------------------------------------------------------

# Muestra todos los productos registrados.
def lista_productos(request):
    # Consultamos los productos y los ordenamos por ID.
    productos = Producto.objects.all().order_by('id')

    # Enviamos los productos a la plantilla que muestra el listado.
    return render(
        request,
        'lista_productos.html',
        {'productos': productos}
    )


# Permite registrar un producto nuevo.
def nuevo_producto(request):
    # Si el usuario envió el formulario, recibimos los datos mediante POST.
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)

        # Verificamos que los datos sean válidos antes de guardarlos.
        if formulario.is_valid():
            formulario.save()

            # Después de guardar, regresamos al listado de productos.
            return redirect('lista_productos')
    else:
        # Si es una petición GET, mostramos un formulario vacío.
        formulario = ProductoForm()

    # Mostramos la plantilla de registro y enviamos el formulario.
    return render(
        request,
        'nuevo_producto.html',
        {'formulario': formulario}
    )


# Permite modificar un producto existente.
def editar_producto(request, pk):
    # Buscamos el producto por su clave primaria.
    # Si no existe, Django devuelve una página 404.
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == 'POST':
        # Cargamos los datos enviados sobre el producto existente.
        formulario = ProductoForm(request.POST, instance=producto)

        if formulario.is_valid():
            formulario.save()
            return redirect('lista_productos')
    else:
        # En una petición GET mostramos el formulario con los datos actuales.
        formulario = ProductoForm(instance=producto)

    return render(
        request,
        'editar_producto.html',
        {
            'formulario': formulario,
            'producto': producto,
        }
    )


# Elimina un producto después de confirmar la acción.
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    # La eliminación se realiza únicamente cuando se confirma mediante POST.
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')

    # Si todavía no se confirmó, mostramos la pantalla de confirmación.
    return render(
        request,
        'eliminar_producto.html',
        {'producto': producto}
    )


# ------------------------------------------------------------
# CATEGORÍAS
# ------------------------------------------------------------

# Muestra todas las categorías registradas.
def lista_categorias(request):
    categorias = Categoria.objects.all().order_by('id')

    return render(
        request,
        'lista_categorias.html',
        {'categorias': categorias}
    )


# Permite registrar una categoría nueva.
def nueva_categoria(request):
    if request.method == 'POST':
        formulario = CategoriaForm(request.POST)

        # Validamos y guardamos la nueva categoría.
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_categorias')
    else:
        # Para una petición GET se crea un formulario vacío.
        formulario = CategoriaForm()

    return render(
        request,
        'nueva_categoria.html',
        {'formulario': formulario}
    )


# Permite modificar una categoría existente.
def editar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)

    if request.method == 'POST':
        # Utilizamos instance para actualizar la categoría encontrada.
        formulario = CategoriaForm(request.POST, instance=categoria)

        if formulario.is_valid():
            formulario.save()
            return redirect('lista_categorias')
    else:
        # Mostramos el formulario con los datos actuales.
        formulario = CategoriaForm(instance=categoria)

    return render(
        request,
        'editar_categoria.html',
        {
            'formulario': formulario,
            'categoria': categoria,
        }
    )


# Elimina una categoría después de confirmar la acción.
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
