from django.urls import path

from . import views

app_name = 'app_zavod'
urlpatterns = [
    # path('', views.all_products, name ='all_products'),
    path('', views.Home, name='home'),
    path('registrar/', views.CreateUser.as_view(), name='registrar_usuario'),
    
]