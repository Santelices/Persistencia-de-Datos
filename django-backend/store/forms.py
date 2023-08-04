from django import forms
from .models import Cuadro
from sale.models import Cliente

class CuadroForm(forms.ModelForm):
    class Meta:
        model = Cuadro
        fields = ['codigo', 'categoria','titulo','descripcion','autor','año','imagen']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'categoria': forms.SelectMultiple(attrs={'class': 'form-control form-control-sm'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'autor': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'año': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'imagen': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),



        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['codigo', 'nombre','telefono','direccion','email']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'email': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        }
