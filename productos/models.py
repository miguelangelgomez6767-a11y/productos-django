# Importamos el módulo de modelos de Django para crear las tablas de la base de datos.
from django.db import models


# Modelo que representa un producto de la tienda.
class Producto(models.Model):
    # Nombre del producto.
    nombre = models.CharField(max_length=100)

    # Categoría a la que pertenece el producto.
    categoria = models.CharField(max_length=100)

    # Precio del producto. Se permiten hasta 10 dígitos y 2 decimales.
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    # Cantidad disponible en inventario.
    cantidad = models.IntegerField()

    # Estado del producto: True = activo, False = inactivo.
    # Por defecto, todos los productos nuevos quedan activos.
    estado = models.BooleanField(default=True)

    # Este método indica qué texto se mostrará cuando Django represente el objeto.
    def __str__(self):
        return self.nombre


# Modelo que representa una categoría de productos.
class Categoria(models.Model):
    # Nombre de la categoría.
    nombre = models.CharField(max_length=100)

    # Observaciones adicionales. blank=True permite dejar este campo vacío.
    observaciones = models.TextField(blank=True)

    # Devuelve el nombre de la categoría como representación del objeto.
    def __str__(self):
        return self.nombre
