from django.urls import path
from .views import home
from .views import galeria
from .views import producto
from .views import carro
from .views import contacto

urlpatterns = [
    path('',home,name="home"),
    path('/galeria',galeria,name="galeria"),
    path('/producto',producto,name="producto"),
    path('/carro',carro,name="carro"),
    path('/contacto',contacto,name="contacto"),
]