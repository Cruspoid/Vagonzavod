from django.urls import path

from . import views

app_name = 'app_zavod'
urlpatterns = [
    # path('', views.all_products, name ='all_products'),
    path('', views.Home, name='home'),
    path('productos/', views.Productos, name='productos'),
    path('detalle_producto/<pk>/', views.DetalleProducto.as_view(), name='detalle_producto'),

    path('objetos-admin/', views.ListObj.as_view(), name='obj_adm'),

    
]