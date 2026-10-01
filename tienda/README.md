# Sistema de Productos

Aplicación web desarrollada con Django para registrar y consultar productos y gestionar categorías.

## Descripción

El proyecto permite:

- Registrar productos.
- Listar productos registrados.
- Guardar el estado de cada producto como un valor booleano (activo/inactivo).
- Registrar categorías.
- Listar categorías.
- Modificar categorías.
- Eliminar categorías.

### Producto

Cada producto contiene:

- Nombre
- Categoría
- Precio
- Cantidad disponible
- Estado (booleano)

### Categoría

Cada categoría contiene:

- Nombre
- Observaciones

## Tecnologías

- Python
- Django
- SQLite
- HTML
- CSS
- Git
- GitHub

## Ejecución

### 1. Crear entorno virtual

```bash
python -m venv venv
```

### 2. Activar el entorno virtual

En Windows:

```bash
venv\Scripts\activate
```

En macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Instalar Django

```bash
pip install django
```

### 4. Aplicar migraciones

```bash
python manage.py migrate
```

### 5. Ejecutar el servidor

```bash
python manage.py runserver
```

Después abre:

- Productos: `http://127.0.0.1:8000/`
- Categorías: `http://127.0.0.1:8000/categorias/`
