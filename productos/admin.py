# Importamos el panel administrativo de Django.
from django.contrib import admin

# Importamos los modelos que queremos administrar desde /admin/.
from .models import Categoria, Producto


# Registramos y configuramos el modelo Producto en el administrador.
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # Columnas que aparecerán en el listado del administrador.
    list_display = ('nombre', 'categoria', 'precio', 'cantidad', 'estado')

    # Permite filtrar productos por su estado.
    list_filter = ('estado',)

    # Campos que pueden utilizarse para realizar búsquedas.
    search_fields = ('nombre', 'categoria')


# Registramos y configuramos el modelo Categoria.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    # Columnas visibles en el listado de categorías.
    list_display = ('nombre', 'observaciones')

    # Campos disponibles para realizar búsquedas.
    search_fields = ('nombre', 'observaciones')
