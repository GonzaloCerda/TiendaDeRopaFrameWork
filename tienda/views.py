from django.shortcuts import render, redirect
from .models import Producto, Catalogo, Oferta
from .forms import  ProductoForm, CatalogoForm, OfertaForm

# Create your views here.

def home(request):
    listaCatalogo = Catalogo.objects.all()
    datos = {
        'Catalogo':listaCatalogo
    }
    return render(request,'tienda/index.html',datos)

def galeria(request, id):
    listaproducto = Producto.objects.filter(catalogo=id)
    datos = {
        'producto':listaproducto,
    }
    return render(request,'tienda/ropa_hombre.html',datos)

def producto(request, id):
    listaproducto = Producto.objects.filter(id_Producto=id)
    datos = {
        'producto':listaproducto
    }
    return render(request,'tienda/hombre1.html',datos)

def oferta(request, id):
    listaoferta = Oferta.objects.filter(id_Oferta=id)
    datos = {
        'oferta':listaoferta
    }
    return render(request,'tienda/ropa_hombre.html',datos)

def carro(request):
    context = {"choclo":"palta"}
    return render(request,'tienda/tienda.html',context)

def menu(request):
    context = {"choclo":"palta"}
    return render(request,'tienda/menu.html',context)

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

####################### CATALOGOS ####################### 

def listadoCatalogo(request):
    listacatalogo = Catalogo.objects.all()
    datos = {
        'Catalogo':listacatalogo
    }
    return render(request,'tienda/listacatalogo.html',datos)

def form_catalogo(request):
    datos = {
        'form':CatalogoForm()
    }

    if(request.method == 'POST'):
        formulario = CatalogoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Guardados correctamente'
    return render(request,'tienda/form_catalogo.html',datos)

def form_mod_catalogo(request, id):
    catalogo = Catalogo.objects.get(id_Catalogo=id)

    datos = {
        'form':CatalogoForm(instance=catalogo)
    }

    if(request.method == 'POST'):
        formulario = CatalogoForm(data=request.POST, instance=catalogo)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Modificados correctamente'
        
    return render(request, 'tienda/form_mod_catalogo.html',datos)

def form_del_catalogo(request, id):
    catalogo = Catalogo.objects.get(id_Catalogo=id)
    catalogo.delete()

    return redirect(to='listacatalogo')

###############Ofertas######################

def listadoOferta(request):
    listaoferta = Oferta.objects.all()
    datos = {
        'oferta':listaoferta
    }
    return render(request,'tienda/listaoferta.html',datos)

def form_oferta(request):
    datos = {
        'form':OfertaForm()
    }

    if(request.method == 'POST'):
        formulario = OfertaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Guardado correctamente'            
    return render(request,'tienda/form_oferta.html',datos)

def form_mod_oferta(request, id):
    oferta = Oferta.objects.get(id_Oferta=id)

    datos = {
        'form':OfertaForm(instance=oferta)
    }

    if(request.method == 'POST'):
        formulario = OfertaForm(data=request.POST, instance=oferta)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Modificados correctamente'
        
    return render(request, 'tienda/form_mod_oferta.html',datos)

def form_de_la_oferta(request, id):
    oferta = Oferta.objects.get(id_Oferta=id)
    oferta.delete()

    return redirect(to='listaoferta')