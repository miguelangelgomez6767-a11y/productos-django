# Importamos el panel administrativo de Django.
from django.contrib import admin

# path crea rutas y include permite conectar las URLs de una aplicación.
from django.urls import path, include


# Rutas principales del proyecto.
urlpatterns = [
    # Ruta para acceder al administrador de Django.
    path('admin/', admin.site.urls),

    # Conectamos las URLs de la aplicación productos con la raíz del proyecto.
    path('', include('productos.urls')),
]
