# Configuración ASGI para ejecutar el proyecto con servidores compatibles con ASGI.
import os

from django.core.asgi import get_asgi_application


# Indicamos el módulo de configuración que utilizará Django.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tienda.settings')

# Creamos la aplicación ASGI que será utilizada por el servidor.
application = get_asgi_application()
