from django.shortcuts import render
from .models import Producto

# Create your views here.

def home(request):
    listaproducto = Producto.objects.all()
    datos = {
        'producto':listaproducto
    }
    return render(request,'tienda/index.html',datos)

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
