
from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import Producto, Catalogo, Oferta

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombreProducto','precio','stock','talla','imgProducto','catalogo']

class CatalogoForm(ModelForm):
    class Meta:
        model = Catalogo
        fields = ['nombreCatalogo','imgCatalogo']

class OfertaForm(ModelForm):
    class Meta:
        model = Oferta
        fields = ['nombreProducto','precio','descuento','precioDescuento','stock','talla','imgProducto','catalogo']