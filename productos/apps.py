# Importamos la clase base para configurar una aplicación Django.
from django.apps import AppConfig


# Configuración de la aplicación productos.
class ProductosConfig(AppConfig):
    # Nombre interno de la aplicación.
    name = 'productos'
