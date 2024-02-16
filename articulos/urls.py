from django.urls import path
from articulos.views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('contactanos/', contactanos, name="contactanos"),
    path('mision/', mision, name="mision"),
    path('pago/', pago, name="pago"),
    path('tienda/', tienda, name="tienda"),
    path('crear/', crear, name="crear"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('modificar/<id>', modificar, name="modificar"),
    path('registrar/',registrar,name="registrar"),
    path('mostrarAdmin/',mostrarAdmin, name="mostrarAdmin"),
    path('mostrarUsuario/',mostrarUsuario, name="mostrarUsuario"),
    path('boletas/', buscar_boletas_por_usuario, name='boletas_usuario'),
    

    path('generarBoleta/', generarBoleta,name="generarBoleta"),
    path('agregar/<id>', agregar_producto, name="agregar"),
    path('eliminar/<id>', eliminar_producto, name="eliminar"),
    path('restar/<id>', restar_producto, name="restar"),
    path('limpiar/', limpiar_carrito, name="limpiar"),
]
