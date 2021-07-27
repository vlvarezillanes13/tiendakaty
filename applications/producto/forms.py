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
            'precio': forms.TextInput(
                attrs = {
                    'placeholder': 'Precio...',
                    'class':'form-control'
                }
            ),
            'imagen': forms.ClearableFileInput(
                attrs = {
                    'placeholder': 'Precio...',
                    'class':'form-control'
                }
            ),

        }
    # validations  
    def clean_precio(self):
        precio_valid= self.cleaned_data['precio']
        precio = int(precio_valid.replace(".",''))
        if not precio > 0:
            raise forms.ValidationError('Ingrese un precio compra mayor a cero')
        else:
            precio = precio_valid
        return precio
    