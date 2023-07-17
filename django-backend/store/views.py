from django.shortcuts import render , redirect
from .models import Cuadro
from .models import Categoria
# Create your views here.

def home(request):
    CuadrosListado = Cuadro.objects.all()
    CategoriaListado = Categoria.objects.all()
    return render(request,'store/gestioncuadros.html',{'cuadros': CuadrosListado , 'categorias' : CategoriaListado})

def registarCuadro(request):
    codigo = request.Post['txtcodigo']
    categoria = request.Post['txtCategoria']
    titulo = request.Post['txttitulo']
    descripcion = request.Post['txtdescripcion']
    autor = request.Post['txtautor']
    año = request.Post['numAño']

    cuadro = Cuadro.objects.create(codigo = codigo , categoria = categoria , titulo = titulo ,descripcion = descripcion , autor = autor, año = año )
    return redirect('/')