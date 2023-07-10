from django.contrib import admin
from .models import *
# Register your models here.



class CategoriaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Datos de Pago', {
            'fields': [
                ('codigo',),
                ('nombre',)
            ]
        }),
    ]

    list_display = (
        'codigo',
        'nombre',
    )
    list_per_page = 20
    search_fields = ('codigo','nombre',)
    list_filter = (
        'codigo',
    )

admin.site.register(Categoria,CategoriaAdmin)


class ProveedorAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Datos de Pago', {
            'fields': [
                ('codigo',),
                ('nombre',),
                ('telefono'),
                ('direccion','email')
            ]
        }),
    ]

    list_display = (
        'codigo',
        'nombre',
        'telefono',
        'direccion',
        'email'

    )
    list_per_page = 20
    search_fields = ('codigo','nombre',)
    list_filter = (
        'codigo',
    )
admin.site.register(Proveedor,ProveedorAdmin)

class CompraAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Datos de Pago', {
            'fields': [
                ('numero',),
                ('proveedor','fecha'),
                ('impuesto','descuento'),
                ('subtotal','total')
            ]
            
        
        })
        ,
    ]

    list_display = (
        'numero',
        'proveedor',
        'fecha',
        'impuesto',
        'descuento',
        'subtotal',
        'total'


    )
    list_per_page = 20
    search_fields = ('numero','fecha','proveedor')
    list_filter = (
        'numero', 'fecha', 'proveedor'
    )
admin.site.register(Compra,CompraAdmin)

class CuadroAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Datos de Pago', {
            'fields': [
                ('codigo',),
                ('categoria','titulo'),
                ('descripcion','autor'),
                ('año')
            ]
            
        
        })
        ,
    ]

    list_display = (
        'codigo',
        'categoria',
        'titulo',
        'descripcion',
        'autor',
        'año',


    )
    list_per_page = 20
    search_fields = ('codigo','categoria','año','autor')
    list_filter = (
        'codigo', 'categoria', 'autor'
    )
admin.site.register(Cuadro,CuadroAdmin)

class MaterialAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Datos de Pago', {
            'fields': [
                ('codigo',),
                ('compra','nombre'),
                ('descripcion','estado'),
            ]
            
        
        })
        ,
    ]

    list_display = (
        'codigo',
        'compra',
        'nombre',
        'descripcion',
        'estado',


    )
    list_per_page = 20
    search_fields = ('codigo','compra','estado',)
    list_filter = (
        'codigo', 'compra', 'estado'
    )
admin.site.register(Material,MaterialAdmin)

class InventarioAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Datos de Pago', {
            'fields': [
                ('codigo',),
                ('fecha_entrada','fecha_salida'),
                ('compra','material'),
            ]
            
        
        })
        ,
    ]

    list_display = (
        'codigo',
        'fecha_entrada',
        'fecha_salida',
        'compra',
        'material',


    )
    list_per_page = 20
    search_fields = ('codigo','compra','material',)
    list_filter = (
        'codigo', 'compra', 'material'
    )
admin.site.register(Inventario,InventarioAdmin)




