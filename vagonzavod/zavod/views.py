from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from .models import Cliente, Producto, Imagenes
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.


def Home(request):
    home = Imagenes.objects.all()
    context = {'home':home}
    return render(request, 'home.html', context)

def Productos(request):
    producto = Producto.objects.all()
    context = {'producto':producto}
    return render(request, 'productos.html', context)


# class CreateUser(CreateView):
#     model = Cliente
#     template_name = "registro.html"
#     form_class = UserRegisterForm
   
#     success_url = reverse_lazy('app_zavod:home')
    
#     def form_valid(self, form):
#         #logica del proceso
#         cliente = form.save()
#         cliente.save()
#         return super(CreateUser, self).form_valid(form)

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
    
    
    
class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
            return self.request.user.is_staff


class ListObj(StaffRequiredMixin, ListView):
           
    template_name = 'objetos_admin.html'
    login_url = reverse_lazy('users_app:user_login')
    paginate_by = 5
    ordering = 'idProducto'
    context_object_name = 'productos'
    
    def get_queryset(self):

        palabra_clave = self.request.GET.get("kword",'')
        
        lista = Producto.objects.filter(
            nombre_producto__icontains=palabra_clave
        )
        return lista