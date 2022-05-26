from django.shortcuts import render
from django.views.generic import CreateView, DetailView
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
    success_url = reverse_lazy('app_zavod:home')
    
    def form_valid(self, form):
        #logica del proceso
        cliente = form.save()
        cliente.save()
        return super(CreateUser, self).form_valid(form)

class DetalleProducto(DetailView):
    model = Producto
    template_name = "detalle_producto.html"
    
    def get_context_data(self, **kwargs):
        context = super(DetalleProducto, self).get_context_data(**kwargs)
        context['titulo'] = 'Motor del mes'
        return context

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        lista = Producto.objects.filter(
            idProducto__icontains=palabra_clave
        )
        return lista
    