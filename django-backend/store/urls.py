from django.urls import path
from .views import CuadroListView

urlpatterns = [
    path('productos', CuadroListView.as_view(), name='productos'),
]