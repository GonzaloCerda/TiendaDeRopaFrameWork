# Generated by Django 3.2.4 on 2021-07-14 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id_Oferta', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID del producto')),
                ('nombreProducto', models.CharField(max_length=50, verbose_name='Nombre del Producto')),
                ('precio', models.IntegerField(verbose_name='Precio')),
                ('descuento', models.IntegerField(verbose_name='Descuento')),
                ('precioDescuento', models.IntegerField(verbose_name='Precio con Descuento')),
                ('stock', models.IntegerField(null=True, verbose_name='Stock')),
                ('talla', models.CharField(max_length=4, null=True, verbose_name='Talla')),
                ('imgProducto', models.ImageField(blank=True, default='tienda/static/tienda/img/no_img.jpg', null=True, upload_to='media/producto')),
                ('catalogo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.catalogo', verbose_name='Nombre de la categoria')),
            ],
        ),
    ]
