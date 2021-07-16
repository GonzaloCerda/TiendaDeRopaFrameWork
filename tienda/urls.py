from django.urls import path, include
from .views import home
from .views import galeria
from .views import producto
from .views import oferta
from .views import carro
from .views import contacto
from .views import listado
from .views import menu
from .views import form_producto, form_mod_producto, form_del_producto
from .views import listadoCatalogo, form_catalogo, form_mod_catalogo, form_del_catalogo
from .views import listadoOferta, form_oferta, form_mod_oferta, form_de_la_oferta
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',home,name="home"),
    path('galeria/<id>',galeria,name="galeria"),
    path('producto/<id>',producto,name="producto"),
    path('oferta/<id>',oferta,name="oferta"),
    path('carro/',carro,name="carro"),
    path('menu/',menu,name="menu"),
    path('contacto/',contacto,name="contacto"),
    path('lista/',listado,name="lista"),
    path('form_producto/',form_producto,name="form_producto"),
    path('form_mod_producto/<id>',form_mod_producto,name="form_mod_producto"),
    path('form_del_producto/<id>',form_del_producto,name="form_del_producto"),
    path('listacatalogo/',listadoCatalogo,name="listacatalogo"),
    path('form_catalogo/',form_catalogo,name="form_catalogo"),
    path('form_mod_catalogo/<id>',form_mod_catalogo,name="form_mod_catalogo"),
    path('form_del_catalogo/<id>',form_del_catalogo,name="form_del_catalogo"),
    path('form_oferta/',form_oferta,name="form_oferta"),
    path('form_de_la_oferta/<id>',form_de_la_oferta,name="form_de_la_oferta"),
    path('form_mod_oferta/<id>',form_mod_oferta,name="form_mod_oferta"),
    path('listaoferta/',listadoOferta,name="listaoferta"),
    path('api/',include('rest_producto.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)