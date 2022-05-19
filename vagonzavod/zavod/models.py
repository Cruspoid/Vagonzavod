from pyexpat import model
from django.db import models

# Create your models here.

class Pedido(models.Model):
    idpedido = models.IntegerField(primary_key = True,verbose_name = 'Id de pedido')
    EstadoP = models.CharField(max_length = 20, verbose_name = 'EstadoP' )
    def __str__(self):
        return self.Pedido

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key = True,verbose_name = 'Id de producto')
    Nombre_producto = models.CharField(max_length = 20, verbose_name = 'N_producto')
    valor = models.IntegerField(max_length=15,verbose_name="valor")
    cantidad = models.IntegerField(max_length=10,verbose_name="cantidad")
    def __str__(self):
        return self.Producto

class Estado(models.Model):
    idEstado = models.IntegerField(primary_key = True,verbose_name = 'Id de Estado')
    estado = models.CharField(max_length = 20, verbose_name = 'Estado' )
    def __str__(self):
        return self.Estado

class Empleado(models.Model):
    Rut_empleado = models.CharField(max_length=12,verbose_name="RUT")
    Nombre = models.CharField(max_length=100, verbose_name = "empleado" )
    apaterno = models.CharField(max_length=50, verbose_name= "apellido paterno" )
    amaterno = models.CharField(max_length=50, verbose_name= "apellido materno" )
    def __str__  (self):
        return self.Empleado


