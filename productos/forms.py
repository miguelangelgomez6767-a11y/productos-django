from django import forms
from .models import Producto, Categoria


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'precio', 'cantidad', 'estado']

        labels = {
            'nombre': 'Nombre del producto',
            'categoria': 'Categoría',
            'precio': 'Precio',
            'cantidad': 'Cantidad disponible',
            'estado': 'Activo',
        }

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

            'estado': forms.CheckboxInput(),
        }


class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ['nombre', 'observaciones']

        labels = {
            'nombre': 'Nombre de la categoría',
            'observaciones': 'Observaciones',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ej: Alimentos'
            }),
            'observaciones': forms.Textarea(attrs={
                'placeholder': 'Escribe observaciones de la categoría',
                'rows': 4
            }),
        }
