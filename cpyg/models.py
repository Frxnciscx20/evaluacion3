'''from django.db import models

# Create your models here.
class NomPro(models.Model):
    idPro=models.IntegerField(primary_key=True, verbose_name='Id Producto')
    nomProducto=models.CharField(max_length=60, verbose_name='Nombre del Producto')

class Producto(models.Model):
    nombre=models.ForeingKey(NomPro, on_delete=models.CASCADE, verbose_name='Nombre')
    codigo= models.IntegerField(primary_key=True, verbose_name='Codigo Producto')
    marca= models.CharField(max_lengh=20, verbose_name='Marca')
    precio= models.IntegerField(max_length=6, verbose_name='Precio')'''