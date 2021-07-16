from rest_framework import serializers
from tienda.models import Producto, Catalogo, Oferta

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['nombreProducto','precio','stock','talla','imgProducto','catalogo']


class CatalogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogo
        fields = ['nombreCatalogo','imgCatalogo']
