from django.shortcuts import render, redirect
from .models import Alimento, Boleta, detalle_boleta
from .forms import AlimentoForm,RegistroUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test
from articulos.compra import Carrito
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model

# Create your views here.

# VISTAS GENERALES

def inicio(request):
    return render(request,'inicio.html')

def mision(request):
    return render(request,'mision.html')

def pago(request):
    return render(request,'pago.html')

def contactanos(request):
    return render(request,'contactanos.html')

def tienda(request):
    return render(request,'tienda.html')

def registrar(request):
    data={
        'form':RegistroUserForm()
    }
    if request.method=="POST":
        formulario=RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request,user)
            return redirect ('inicio')
        data["form"]=formulario   
    return render(request,'registration/registrar.html', data)

def mostrarUsuario(request):
    articulos=Alimento.objects.all()
    paginator = Paginator(articulos,8)
    page_number = request.GET.get('page',1)
    page = paginator.get_page(page_number)
    datos={
        'articulos':page
    }
    return render(request,'mostrarUsuario.html', datos)

# VISTAS DE USUARIO

from django.contrib.auth.decorators import login_required

"""@login_required
def buscar_boletas_por_usuario(request):
    usuario = request.user.username

    boletas = Boleta.objects.filter(usuario=usuario).prefetch_related('detalle_boleta')

    boletas_data = []

    for boleta in boletas:
        boleta_data = {
            'id_boleta': boleta.id_boleta,
            'total': boleta.total,
            'fechaCompra': boleta.fechaCompra,
            'estado': boleta.estado,
            'usuario': boleta.usuario,
            'detalles': []
        }

        detalles = boleta.detalle_boleta.all()
        for detalle in detalles:
            detalle_data = {
                'nombre': detalle.nombre,
                'id_producto': detalle.id_producto,
                'cantidad': detalle.cantidad,
                'subtotal': detalle.subtotal
            }
            boleta_data['detalles'].append(detalle_data)

        boletas_data.append(boleta_data)

    context = {
        'boletas': boletas_data
    }

    return render(request, 'boletas_usuario.html', context)
"""
@login_required
def buscar_boletas_por_usuario(request):
    usuario = request.user.username

    boletas = Boleta.objects.filter(usuario=usuario)

    boletas_data = []

    for boleta in boletas:
        boleta_data = {
            'id_boleta': boleta.id_boleta,
            'total': boleta.total,
            'fechaCompra': boleta.fechaCompra,
            'estado': boleta.estado,
            'usuario': boleta.usuario,
        }

        boletas_data.append(boleta_data)

    context = {
        'boletas': boletas_data
    }

    return render(request, 'boletas_usuario.html', context)

@login_required
def agregar_producto(request,id):
    carrito_compra= Carrito(request)
    alimento = Alimento.objects.get(cod=id)
    carrito_compra.agregar(alimento)
    return redirect('mostrarUsuario')

@login_required
def eliminar_producto(request, id):
    carrito_compra= Carrito(request)
    alimento = Alimento.objects.get(cod=id)
    carrito_compra.eliminar(alimento)
    return redirect('mostrarUsuario')

@login_required
def restar_producto(request, id):
    carrito_compra= Carrito(request)
    alimento = Alimento.objects.get(cod=id)
    carrito_compra.restar(alimento)
    return redirect('mostrarUsuario')

@login_required
def limpiar_carrito(request):
    carrito_compra= Carrito(request)
    carrito_compra.limpiar()
    return redirect('mostrarUsuario')    

from django.contrib.auth.decorators import login_required

@login_required
def generarBoleta(request):
    precio_total = 0
    for key, value in request.session['carrito'].items():
        precio_total = precio_total + int(value['precio']) * int(value['cantidad'])
        impuestos = round(precio_total * 0.19)
        envio = round(precio_total * 0.02)

    User = get_user_model()
    user = User.objects.get(pk=request.user.pk)

    boleta = Boleta(total=precio_total, usuario=user)
    boleta.estado = "Procesando Pedido"
    productos = []
    for key, value in request.session['carrito'].items():
        producto = Alimento.objects.get(cod=value['articulo_id'])
        boleta.save()
        nombre = value['nombre']
        cant = value['cantidad']
        subtotal = cant * int(value['precio'])
        detalle = detalle_boleta(id_boleta=boleta, id_producto=producto, nombre=nombre, cantidad=cant, subtotal=subtotal)
        detalle.save()
        productos.append(detalle)

    datos = {
        'productos': productos,
        'fecha': boleta.fechaCompra,
        'impuestos': impuestos,
        'envio': envio,
        'total': boleta.total,
        'estado': boleta.estado,
        'usuario': boleta.usuario,
        'nombre': nombre
    }

    if cant >= 1:
        producto.stock -= int(value['cantidad'])
        producto.save()
        request.session['boleta'] = boleta.id_boleta
        carrito = Carrito(request)
        carrito.limpiar()

        return render(request, 'detallecarrito.html', datos)
    else:
        producto.stock -= 1
        producto.save()
        request.session['boleta'] = boleta.id_boleta
        carrito = Carrito(request)
        carrito.limpiar()

        return render(request, 'detallecarrito.html', datos)

   



# VISTAS DE ADMIN

@user_passes_test(lambda u: u.is_superuser)
def crear(request):
    if request.method=="POST":
        alimentoform = AlimentoForm(request.POST,request.FILES) #Asigna objeto alimentoform
        if alimentoform.is_valid():
            alimentoform.save() 
            return redirect ('mostrarAdmin')
    else:
        alimentoform=AlimentoForm() #Sino este crea uno nuevo
    return render(request, 'crear.html', {'alimentoform' : alimentoform})

@user_passes_test(lambda u: u.is_superuser)
def eliminar(request, id):
    alimentoEliminado=Alimento.objects.get(cod=id) #buscamos un vehiculo por la patentes
    alimentoEliminado.delete()
    return redirect('mostrarAdmin')

@user_passes_test(lambda u: u.is_superuser)
def modificar(request,id):
    alimentoModificado = Alimento.objects.get(cod=id)
    datos ={
        'form': AlimentoForm(instance=alimentoModificado)   #el objeto form llega al template
    }
    if request.method=="POST":          #modificamos backend con los cambios realizados
        formulario = AlimentoForm(request.POST,request.FILES, instance=alimentoModificado)
        if formulario.is_valid():
            formulario.save()           #modificamos el objeto
            return redirect('mostrarAdmin')
    return render(request,'modificar.html', datos)

@user_passes_test(lambda u: u.is_superuser)
def mostrarAdmin(request):
    articulos=Alimento.objects.all()
    datos={
        'articulos':articulos
    }
    return render(request,'mostrarAdmin.html', datos)





