from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Cuadro
from django.db.models import Q
# Create your views here.

class CuadroListView(LoginRequiredMixin, ListView):
    login_url = '/segurity/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'store/productos.html'
    context_object_name = 'productos'
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
