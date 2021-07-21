from applications.producto.models import Producto
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    View,
)
# Create your views here.
from .views import(
    Producto,
)



class ProductoListView(ListView):
    template_name = "producto/lista.html"
    context_object_name = 'productos'

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        order = self.request.GET.get("order", '')
        queryset = Producto.objects.buscar_producto(kword, order)
        return queryset