from django.contrib import admin

from .models import Categoria, Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'cantidad', 'estado')
    list_filter = ('estado',)
    search_fields = ('nombre', 'categoria')


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'observaciones')
    search_fields = ('nombre', 'observaciones')
