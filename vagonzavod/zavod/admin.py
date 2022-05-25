from django.contrib import admin
from .models import Pedido, Producto, Estado, Empleado, Cliente

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display=("nombre_cliente","rut_cliente","email_cliente")
    search_fields= ("nombre_cliente","rut_cliente")

    
admin.site.register(Cliente, ClienteAdmin)



admin.site.register(Pedido)
admin.site.register(Producto)
admin.site.register(Estado)
admin.site.register(Empleado)
