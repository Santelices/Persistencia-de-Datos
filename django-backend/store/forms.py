from django import forms
from .models import Cuadro , Categoria
from sale.models import Cliente

class CuadroForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categoria'].widget = forms.Select(attrs={'class': 'form-control form-control-sm'})
        self.fields['categoria'].queryset = Categoria.objects.all()

    class Meta:
        model = Cuadro
        fields = ['codigo', 'categoria', 'titulo', 'descripcion', 'autor', 'año', 'imagen']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'autor': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'año': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control form-control-sm'}),
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
