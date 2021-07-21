from applications.producto.models import Clasificador, Marca, Producto
from django.contrib import admin

# Register your models here.

admin.site.register(Clasificador)
admin.site.register(Producto)
admin.site.register(Marca)