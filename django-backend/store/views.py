from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from .models import Cuadro 
from sale.models import Cliente
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from .forms import CuadroForm , ClienteForm


# Create your views here.

class CuadroListView(LoginRequiredMixin, ListView):
    login_url = '/segurity/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'store/cuadros.html'
    context_object_name = 'cuadros'
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context

    def get_queryset(self, **kwargs):
        search = self.request.GET.get('search', '')
        return Cuadro.objects.filter(
            Q(deleted=False),
            Q(codigo__icontains=search) |
            Q(titulo__icontains=search) |
            Q(autor__icontains=search) |
            Q(año__icontains=search) 
        )

class ClienteListView(LoginRequiredMixin, ListView):
    login_url = '/segurity/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'store/clientes.html'
    context_object_name = 'clientes'
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context

    def get_queryset(self, **kwargs):
        search = self.request.GET.get('search', '')
        return Cliente.objects.filter(
            Q(deleted=False),
            Q(codigo__icontains=search) |
            Q(nombre__icontains=search) |
            Q(telefono__icontains=search) |
            Q(direccion__icontains=search) |
            Q(email__icontains=search)
        )


class CuadroCreateView(LoginRequiredMixin, CreateView):
    login_url = '/seguridad/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'store/cuadroform.html'
    form_class = CuadroForm


    def form_valid(self, form):
        form.instance.creado_por = self.request.user
        return super().form_valid(form)

    def get_success_url(self):

        return '/store/cuadros'
    
class ClienteCreateView(LoginRequiredMixin, CreateView):
    login_url = '/seguridad/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'store/clienteform.html'
    form_class = ClienteForm


    def form_valid(self, form):
        form.instance.creado_por = self.request.user
        return super().form_valid(form)

    def get_success_url(self):

        return '/store/clientes'