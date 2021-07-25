from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = (
            'nombre',
            'marca',
            'clasificador',
            'descripcion',
            'precio',
            'anulado',
            'imagen'
        )
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'placeholder': 'Nombre...',
                    'class':'form-control'
                }
            ),
            'marca':forms.Select(
                attrs = {
                    'class':"form-select",
                }
            ),
            'clasificador':forms.Select(
                attrs = {
                    'class':"form-select",
                }
            ),
            'descripcion': forms.Textarea(
                attrs = {
                    'placeholder': 'Descripción...',
                    'class':'form-control'
                }
            ),
            'precio': forms.NumberInput(
                attrs = {
                    'placeholder': 'Precio...',
                    'class':'form-control'
                }
            ),

        }
    # validations  
    def clean_precio(self):
        precio= self.cleaned_data['precio']
        if not precio > 0:
            raise forms.ValidationError('Ingrese un precio compra mayor a cero')

        return precio
    