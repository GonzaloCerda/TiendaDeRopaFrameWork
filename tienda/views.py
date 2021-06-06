from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

# Create your views here.

def home(request):
    context = {"choclo":"palta"}
    return render(request,'tienda/index.html',context)

def galeria(request):
    context = {"choclo":"palta"}
    return render(request,'tienda/ropa_hombre.html',context)

def producto(request):
    context = {"choclo":"palta"}
    return render(request,'tienda/hombre1.html',context)

def carro(request):
    context = {"choclo":"palta"}
    return render(request,'tienda/tienda.html',context)

def contacto(request):
    context = {"choclo":"palta"}
    return render(request,'tienda/contacto.html',context)

def listado(request):
    listaproducto = Producto.objects.all()
    datos = {
        'producto':listaproducto
    }
    return render(request,'tienda/listaproductos.html',datos)

def form_producto(request):
    datos = {
        'form':ProductoForm()
    }

    if(request.method == 'POST'):
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Guardados correctamente'
    return render(request,'tienda/form_producto.html',datos)

def form_mod_producto(request, id):
    producto = Producto.objects.get(id_Producto=id)

    datos = {
        'form':ProductoForm(instance=producto)
    }

    if(request.method == 'POST'):
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Modificados correctamente'
        
    return render(request, 'tienda/form_mod_producto.html',datos)

def form_del_producto(request, id):
    producto = Producto.objects.get(id_Producto=id)
    producto.delete()

    return redirect(to='lista')