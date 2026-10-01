#!/usr/bin/env python
"""Punto de entrada para ejecutar comandos administrativos de Django."""

# Módulo para trabajar con variables de entorno y configuración del sistema.
import os

# Módulo para acceder a los argumentos de la línea de comandos.
import sys


# Función principal utilizada para ejecutar comandos como runserver, migrate, etc.
def main():
    # Indicamos a Django qué archivo contiene la configuración del proyecto.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tienda.settings')

    try:
        # Importamos la función que ejecuta los comandos de Django.
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Mostramos un mensaje útil si Django no está instalado o no está disponible.
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Ejecutamos el comando recibido desde la terminal.
    execute_from_command_line(sys.argv)


# Ejecutamos main() únicamente cuando este archivo se inicia directamente.
if __name__ == '__main__':
    main()
