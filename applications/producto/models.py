from django.db import models
from model_utils.models import TimeStampedModel
from .managers import ProductoManager

# Create your models here.

class Clasificador(TimeStampedModel):
    nombre = models.CharField(
        max_length=20,
        unique=True
    )

    class Meta:
        verbose_name = 'Clasificador'
        verbose_name_plural = 'Clasificaciones'

    def __str__(self):
        return self.nombre

class Marca(TimeStampedModel):
    nombre = models.CharField(
        max_length=20,
        unique=True
    )

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.nombre

    

class Producto(TimeStampedModel):
    nombre = models.CharField(
        'Nombre', 
        max_length=40
    )
    marca = models.ForeignKey(
        Marca, 
        on_delete=models.CASCADE
    )
    clasificador = models.ForeignKey(
        Clasificador, 
        on_delete=models.CASCADE
    )
    descripcion = models.TextField(
        'descripcion del producto',
        blank=True,
    )
    precio = models.CharField(
        'precio venta',
        max_length=10
    )
    anulado = models.BooleanField(
        'eliminado',
        default=False
    )
    imagen = models.ImageField(
        upload_to="Productos", 
        blank=False, 
        null=False,
        default= '/default/default-prod.png'
    )
    #processors=[ResizeToFill(100, 50)],

    objects = ProductoManager()

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        unique_together = [['nombre', 'marca']]


    def __str__(self):
        return self.nombre