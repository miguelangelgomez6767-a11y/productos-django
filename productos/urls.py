# Importamos path para definir las rutas de la aplicación.
from django.urls import path

# Importamos las vistas que responderán a cada URL.
from . import views


# Lista de URLs disponibles dentro de la aplicación productos.
urlpatterns = [
    # Página principal: muestra el listado de productos.
    path('', views.lista_productos, name='lista_productos'),

    # Crear, editar y eliminar productos.
    path('productos/nuevo/', views.nuevo_producto, name='nuevo_producto'),
    path('productos/<int:pk>/editar/', views.editar_producto, name='editar_producto'),
    path('productos/<int:pk>/eliminar/', views.eliminar_producto, name='eliminar_producto'),

    # Crear, editar y eliminar categorías.
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/nueva/', views.nueva_categoria, name='nueva_categoria'),
    path('categorias/<int:pk>/editar/', views.editar_categoria, name='editar_categoria'),
    path('categorias/<int:pk>/eliminar/', views.eliminar_categoria, name='eliminar_categoria'),
]
