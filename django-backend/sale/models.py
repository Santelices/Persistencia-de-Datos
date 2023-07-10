from django.db import models
from store.models import *
from segurity.models import ModelBase,ModelBaseAudited
# Create your models here.

class Cliente(ModelBaseAudited):
    codigo = models.CharField(max_length=100,blank=True,null=True)
    nombre = models.CharField(max_length=100,blank=True,null=True)
    telefono = models.CharField(max_length=20,blank=True,null=True)
    direccion = models.CharField(max_length=1024,blank=True,null=True)
    email = models.CharField(max_length=100,blank=True,null=True)

    class Meta :
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['-nombre']

    def __str__(self):
        return self.nombre
    
class Pago(ModelBase):
    codigo = models.CharField(max_length=100,blank=True,null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta :
        ordering = ['-nombre']

    def __str__(self):
        return self.nombre

class Venta(ModelBaseAudited):
    numero = models.CharField(max_length=20, blank=True, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True, null=True)
    pago = models.ForeignKey(Pago, on_delete=models.CASCADE, blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    descuento = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    subtotal = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    class Meta :
       verbose_name = ' Venta'
       verbose_name_plural = 'Ventas'
       ordering = ['-numero']

    def __str__(self):
       return self.numero
    
class DetalleVenta(ModelBaseAudited):
    numero = models.CharField(max_length=20, blank=True, null=True)
    cuadro = models.ForeignKey(Cuadro, on_delete=models.CASCADE, blank=True, null=True)
    venta = models.ForeignKey(Pago, on_delete=models.CASCADE, blank=True, null=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2, default=0, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=8, decimal_places=2, default=0, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=8, decimal_places=2, default=0, blank=True, null=True)
    total = models.DecimalField(max_digits=8, decimal_places=2, default=0, blank=True, null=True)

    class Meta :
       verbose_name = 'Venta Detalle'
       verbose_name_plural = 'Ventas Detalle'
       ordering = ['-venta']


    def __str__(self):
       return self.producto