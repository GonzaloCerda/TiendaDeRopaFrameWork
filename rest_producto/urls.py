from django.urls import path
from rest_producto.views import lista_producto
from rest_producto.views import lista_catalogo
from rest_producto.views import detalle_producto
from rest_producto.views import detalle_catalogo
from rest_producto.viewsLogin import login

urlpatterns = [
    path('lista_producto',lista_producto,name='lista_producto'),
    path('lista_catalogo',lista_catalogo,name='lista_catalogo'),
    path('detalle-producto/<id>',detalle_producto,name='detalle_producto'),
    path('detalle-catalogo/<id>',detalle_catalogo,name='detalle_catalogo'),
    path('login',login,name='login'),
]