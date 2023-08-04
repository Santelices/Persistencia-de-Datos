from django.db import models
from segurity.models import ModelBase,ModelBaseAudited
from segurity.constants import Gender
# Create your models here.
class Categoria(ModelBase):
    codigo = models.CharField(max_length=100,blank=True,null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta :
        ordering = ['-nombre']

    def __str__(self):
        return self.nombre

class Proveedor(ModelBaseAudited):
    codigo = models.CharField(max_length=100,blank=True,null=True)
    nombre = models.CharField(max_length=100,blank=True,null=True)
    telefono = models.CharField(max_length=20,blank=True,null=True)
    direccion = models.CharField(max_length=1024,blank=True,null=True)
    email = models.CharField(max_length=100,blank=True,null=True)

    class Meta :
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['-nombre']

    def __str__(self):
        return self.nombre

class Compra(ModelBaseAudited):
    numero = models.CharField(max_length=20, blank=True, null=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, blank=True, null=True)
    fecha = models.DateTimeField( blank=True, null=True)
    impuesto = models.DecimalField(max_digits=8, decimal_places=2)
    descuento = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    subtotal = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    class Meta :
       verbose_name = 'Compra'
       verbose_name_plural = 'Compras'
       ordering = ['-numero']

    def __str__(self):
       return self.numero

class Cuadro(ModelBaseAudited):
    codigo = models.CharField(max_length=20, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=True, null=True)
    titulo = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    autor = models.CharField(max_length=100, blank=True, null=True)
    año = models.CharField(max_length=100, blank=True, null=True)
    imagen = models.ImageField(upload_to='Cuadros', null=True)

    class Meta:
        verbose_name = 'Cuadro'
        verbose_name_plural = 'Cuadros'

    def __str__(self):
        return self.titulo

class Material(ModelBaseAudited):
    codigo = models.CharField(max_length=20, blank=True, null=True)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, blank=True, null=True)
    nombre = models.CharField(max_length=100,blank=True,null=True)
    descripcion = models.TextField()
    estado = models.BooleanField()

    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materiales'

    def __str__(self):
        return self.nombre

class Inventario(ModelBaseAudited):
    codigo = models.CharField(max_length=20, blank=True, null=True)
    fecha_entrada =  models.DateTimeField( blank=True, null=True)
    fecha_salida =  models.DateTimeField( blank=True, null=True)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, blank=True, null=True)
    material = models.ForeignKey(Material, on_delete=models.CASCADE, blank=True, null=True)

    class Meta :
       verbose_name = 'Inventario'
       verbose_name_plural = 'Inventarios'
       ordering = ['-codigo']

    def __str__(self):
       return self.codigo
