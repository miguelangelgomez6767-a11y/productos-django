# Importamos el sistema de formularios de Django.
from django import forms

# Importamos los modelos que utilizaremos en los formularios.
from .models import Producto, Categoria


# Formulario para crear y editar productos.
class ProductoForm(forms.ModelForm):

    class Meta:
        # Indicamos que este formulario está basado en el modelo Producto.
        model = Producto

        # Campos que aparecerán en el formulario.
        fields = ['nombre', 'categoria', 'precio', 'cantidad', 'estado']

        # Etiquetas que verá el usuario en pantalla.
        labels = {
            'nombre': 'Nombre del producto',
            'categoria': 'Categoría',
            'precio': 'Precio',
            'cantidad': 'Cantidad disponible',
            'estado': 'Activo',
        }

        # Personalizamos los campos HTML para mostrar ejemplos y restricciones.
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ej: Arroz'
            }),

            'categoria': forms.TextInput(attrs={
                'placeholder': 'Ej: Alimentos'
            }),

            'precio': forms.NumberInput(attrs={
                'placeholder': 'Ej: 5000.00',
                'step': '0.01'
            }),

            'cantidad': forms.NumberInput(attrs={
                'placeholder': 'Ej: 10',
                'min': '0'
            }),

            # Casilla para indicar si el producto está activo.
            'estado': forms.CheckboxInput(),
        }


# Formulario para crear y editar categorías.
class CategoriaForm(forms.ModelForm):

    class Meta:
        # El formulario utiliza el modelo Categoria.
        model = Categoria

        # Campos que se mostrarán al usuario.
        fields = ['nombre', 'observaciones']

        # Textos que aparecerán como etiquetas.
        labels = {
            'nombre': 'Nombre de la categoría',
            'observaciones': 'Observaciones',
        }

        # Personalizamos la apariencia de los campos HTML.
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ej: Alimentos'
            }),
            'observaciones': forms.Textarea(attrs={
                'placeholder': 'Escribe observaciones de la categoría',
                'rows': 4
            }),
        }
