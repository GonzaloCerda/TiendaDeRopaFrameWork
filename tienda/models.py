from django.db import models


# Modelo Catalogo-Producto-Oferta-Pedido.

default_image = 'tienda/static/tienda/img/no_img.jpg'

class Catalogo(models.Model):

   id_Catalogo = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID del catalogo')
   nombreCatalogo = models.CharField(max_length=50,verbose_name='Nombre de la categoria')
   imgCatalogo = models.ImageField(null=True, blank=True, upload_to="media/catalogo" ,default=default_image)
   
   def __str__(self):
      return self.nombreCatalogo

class Producto(models.Model):

   id_Producto = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID del producto')
   nombreProducto = models.CharField(max_length=50, verbose_name='Nombre del Producto')
   precio = models.IntegerField(verbose_name='Precio')
   stock = models.IntegerField(null=True,verbose_name='Stock')
   talla = models.CharField(max_length=4, null=True,verbose_name='Talla')
   imgProducto = models.ImageField(null=True, blank=True, upload_to="media/producto", default=default_image)
   catalogo = models.ForeignKey(Catalogo, on_delete=models.CASCADE,verbose_name='Nombre de la categoria')
    
   def __str__(self):
        return self.nombreProducto

# Modelo Comprador-Pedido-Producto.
class Comprador(models.Model):

    rut = models.CharField(primary_key=True, max_length=10, verbose_name='Rut del Comprador')
    nombre = models.CharField(max_length=35, verbose_name='Nombre')
    apellido = models.CharField(max_length=35, verbose_name='Apellido')
    telefono = models.CharField(max_length=16, verbose_name='Teléfono')
    email = models.CharField(max_length=14, verbose_name='Correo Electrónico')
    ciudad = models.CharField(max_length=50, verbose_name='Ciudad')
    direccion = models.CharField(max_length=50, verbose_name='Dirección')
    
    def __str__(self):
       return self.rut

# Modelo DetallePedido

class Pedido(models.Model):

    id_Pedido = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID del pedido')
    rut = models.ForeignKey(Comprador, on_delete=models.CASCADE)
    
    def __int__(self):
        return self.id_Pedido

class detallePedido(models.Model):

    id_detallePedido = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID del detallePedido')
    codPedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, verbose_name='Codigo de Pedido')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name='Codigo de Producto')
    cantidad = models.IntegerField(verbose_name='Cantidad del producto')

    def __int__(self):
        return self.id_detallePedido
 
class Oferta(models.Model):
      
   id_Oferta = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID de la oferta')
   nombreProducto = models.CharField(max_length=50, verbose_name='Nombre del Producto')
   precio = models.IntegerField(verbose_name='Precio')
   descuento = models.IntegerField(verbose_name='Descuento')
   precioDescuento = models.IntegerField(verbose_name='Precio con Descuento')
   stock = models.IntegerField(null=True,verbose_name='Stock')
   talla = models.CharField(max_length=4, null=True,verbose_name='Talla')
   imgProducto = models.ImageField(null=True, blank=True, upload_to="media/producto", default=default_image)
   catalogo = models.ForeignKey(Catalogo, on_delete=models.CASCADE,verbose_name='Nombre de la categoria')
  
   def __str__(self):
        return self.nombreProducto


