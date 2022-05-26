from django.shortcuts import render
from django.views.generic import CreateView
from .models import Cliente, Producto, Imagenes
from django.urls import reverse_lazy
# Create your views here.


def Home(request):
    home = Imagenes.objects.all()
    context = {'home':home}
    return render(request, 'home.html', context)

def Productos(request):
    producto = Producto.objects.all()
    context = {'producto':producto}
    return render(request, 'productos.html', context)

class CreateUser(CreateView):
    model = Cliente
    template_name = "registro.html"
    fields = [
        'nombre_cliente',
        'apellido_cliente',
        'rut_cliente',
        'email_cliente',
        'contrasena_cliente',
        'confirmar_contrasena_cliente',
        'celular_cliente',
    ]
    success_url = reverse_lazy('app_zavod:registrar_usuario')
    
    def form_valid(self, form):
        #logica del proceso
        cliente = form.save()
        cliente.save()
        return super(CreateUser, self).form_valid(form)

