from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'precio', 'cantidad']

        labels = {
            'nombre': 'Nombre del producto',
            'categoria': 'Categoría',
            'precio': 'Precio',
            'cantidad': 'Cantidad disponible',
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
        }