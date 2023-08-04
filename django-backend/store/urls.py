from django.urls import path
from .views import CuadroListView , ClienteListView , CuadroCreateView , ClienteCreateView


urlpatterns = [
    path('cuadros', CuadroListView.as_view(), name='cuadros'),
    path('clientes', ClienteListView.as_view(), name='clientes'),
    path('store/cuadrosform/', CuadroCreateView.as_view(), name='cuadrosform'),
    path('store/clientesform/', ClienteCreateView.as_view(), name='clientesform'),
]