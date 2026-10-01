# Configuración WSGI para ejecutar Django con servidores compatibles con WSGI.
import os

from django.core.wsgi import get_wsgi_application


# Indicamos dónde se encuentra la configuración principal del proyecto.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tienda.settings')

# Creamos la aplicación WSGI que utilizará el servidor.
application = get_wsgi_application()
