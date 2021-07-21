from django.db import models
from django.db.models import Q

class ProductoManager(models.Manager):
    """ procedimiento modelo product """

    def mostrar_ultimos(self):
        return self.filter(
            anulado = False
        ).order_by('-created')

    def buscar_producto(self, kword, order):
        consulta = self.filter(
            Q(nombre__icontains=kword)
        )
        # verificamos en que orden se solicita
        if order == 'fecha':
            # ordenar por fecha
            return consulta.order_by('created')
        elif order == 'nombre':
            # ordenar por nombre
            return consulta.order_by('nombre')
        else:
            return consulta.order_by('-created')