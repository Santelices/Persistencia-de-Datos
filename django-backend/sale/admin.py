from django.contrib import admin
from .models import *
# Register your models here.

class PagoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Datos de Pago', {
            'fields': [
                ('codigo',),
                ('nombre', 'monto'),
                ('fecha',)
            ]
        }),
    ]

    list_display = (
        'codigo',
        'nombre',
        'monto',
        'fecha',
    )
    list_per_page = 20
    search_fields = ('codigo','nombre','fecha')
    list_filter = (
        'nombre','fecha'
    )

admin.site.register(Pago,PagoAdmin)


class ClienteAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Datos de Pago', {
            'fields': [
                ('codigo',),
                ('nombre', 'telefono'),
                ('direccion','email')
            ]
        }),
    ]

    list_display = (
        'codigo',
        'nombre',
        'direccion',
        'email',
    )
    list_per_page = 20
    search_fields = ('codigo','nombre','direccion','email')
    list_filter = (
        'codigo','direccion','email'
    )

admin.site.register(Cliente,ClienteAdmin)



class VentaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Datos de Pago', {
            'fields': [
                ('numero',),
                ('cliente', 'pago'),
                ('fecha'),
                ('descuento','subtotal','total')
            ]
        }),
    ]

    list_display = (
        'numero',
        'cliente',
        'pago',
        'fecha',
        'descuento',
        'subtotal',
        'total',
    )
    list_per_page = 20
    search_fields = ('numero','cliente','fecha')
    list_filter = (
        'numero','cliente','fecha'
    )

admin.site.register(Venta,VentaAdmin)

class DetalleVentaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Datos de Pago', {
            'fields': [
                ('numero',),
                ('cuadro', 'venta'),
                ('precio'),
                ('cantidad','subtotal','total')
            ]
        }),
    ]

    list_display = (
        'numero',
        'cuadro',
        'venta',
        'precio',
        'cantidad',
        'subtotal',
        'total',
    )
    list_per_page = 20
    search_fields = ('numero','cuadro',)
    list_filter = (
        'numero','cuadro'
    )

admin.site.register(DetalleVenta,DetalleVentaAdmin)

