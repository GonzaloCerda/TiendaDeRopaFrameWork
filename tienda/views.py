from django.shortcuts import render

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
