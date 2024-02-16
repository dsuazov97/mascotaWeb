
from django.db import models
import datetime
from distutils.command.upload import upload
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


# Create your models here.

class TipoMascota(models.Model):
    idMasc= models.IntegerField(primary_key=True, verbose_name="Id TipoMasc")
    nombreTipo= models.CharField(max_length=50, blank=True, verbose_name="Tipo de Mascota")
    
    def __str__(self) -> str:
        return self.nombreTipo
    
class Marca(models.Model):
    idMarca= models.IntegerField(primary_key=True, verbose_name="Id Marca")
    nombreMarca= models.CharField(max_length=50, blank=True, verbose_name="Marca")

    def __str__(self) -> str:
        return self.nombreMarca 
    
class Alimento(models.Model):
    cod= models.CharField(primary_key=True, max_length=5,verbose_name="Codigo")
    nombre= models.CharField(max_length=50, blank=True, verbose_name="Nombre")
    tipo= models.ForeignKey(TipoMascota, on_delete=models.CASCADE, verbose_name="Tipo de Mascota")
    marca= models.ForeignKey(Marca, on_delete=models.CASCADE, verbose_name="Marca")
    imagen= models.ImageField(upload_to="imagenes",null=True , blank=True, verbose_name="Imagen")
    precio= models.IntegerField(validators=[MinValueValidator(0)],default=0,blank=True, verbose_name="Precio")
    stock= models.IntegerField(validators=[MinValueValidator(0)],default=0,blank=True, verbose_name="Stock")

    def __str__(self) -> str:
        return self.cod

class Boleta(models.Model):
    id_boleta=models.AutoField(primary_key=True)
    total=models.BigIntegerField()
    fechaCompra=models.DateTimeField(blank=False, null=False, default = datetime.datetime.now)
    estado=models.CharField(max_length=50, blank=True)
    usuario=models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.id_boleta)

class detalle_boleta(models.Model):
    id_boleta = models.ForeignKey('Boleta', blank=True, on_delete=models.CASCADE)
    id_detalle_boleta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('Alimento', on_delete=models.CASCADE)
    nombre= models.CharField(max_length=50, blank=True)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()

    def __str__(self):
        return str(self.id_detalle_boleta)
    