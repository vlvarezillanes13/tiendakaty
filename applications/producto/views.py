from django.db import models
from applications.producto.models import Producto
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.views.generic.edit import(
     FormView,
)
# Create your views here.
from .views import(
    Producto,
)

from .forms import(
    ProductoForm,
)


class ProductoListView(ListView):
    template_name = "producto/lista.html"
    context_object_name = 'productos'
    paginate_by = 5

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        order = self.request.GET.get("order", '')
        queryset = Producto.objects.buscar_producto(kword, order)
        return queryset
        
class ProductoDetailView(DetailView):
    template_name = "producto/detalle.html"
    model = Producto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #
        return context

class ProductoCreateView(FormView):
    #model = Producto
    template_name = "producto/agregar.html"
    form_class = ProductoForm
    success_url = reverse_lazy('productos:listar-productos')

    def form_valid(self, form):
        nombre  = form.cleaned_data['nombre']
        nombre_edit = nombre[0].upper()+nombre[1::]
        Producto.objects.create(
            nombre=nombre_edit,
            marca=form.cleaned_data['marca'],
            clasificador=form.cleaned_data['clasificador'],
            descripcion=form.cleaned_data['descripcion'],
            precio=form.cleaned_data['precio'],
            anulado=form.cleaned_data['anulado'],
            imagen=form.cleaned_data['imagen']

        )
        return super(ProductoCreateView, self).form_valid(form)


class ProductoDeleteView(DeleteView):
    template_name = "producto/eliminar.html"
    model = Producto
    success_url = reverse_lazy('productos:listar-productos')


class ProductoUpdateView(UpdateView):
    template_name = "producto/actualizar.html"
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy('productos:listar-productos')

    def form_valid(self, form):
        nombre  = form.cleaned_data['nombre']
        nombre_edit = nombre[0].upper()+nombre[1::]
        Producto.objects.update(
            nombre=nombre_edit,
            marca=form.cleaned_data['marca'],
            clasificador=form.cleaned_data['clasificador'],
            descripcion=form.cleaned_data['descripcion'],
            precio=form.cleaned_data['precio'],
            anulado=form.cleaned_data['anulado'],
            imagen=form.cleaned_data['imagen']

        )
        return super(ProductoCreateView, self).form_valid(form)


class ImpresionesPageView(TemplateView):
    template_name = "clasificador/impresiones.html"


class ClasificadorListView(ListView):
    template_name = "clasificador/clasificador.html"
    context_object_name = 'productos'
    #paginate_by = 5

    def get_queryset(self):
        clasificador = self.request.GET.get("clasificador", '')
        queryset = Producto.objects.buscar_producto_clasificador(clasificador)
        return queryset

    def get_context_data(self, **kwargs):
        clasificador = self.request.GET.get("clasificador", '')
        context = super().get_context_data(**kwargs)
        context['clasificador'] = clasificador
        return context


'''
class ProductCreateView(AlmacenPermisoMixin, CreateView):
    template_name = "producto/form_producto.html"
    form_class = ProductForm
    success_url = reverse_lazy('producto_app:producto-lista')


class ProductUpdateView(AlmacenPermisoMixin, UpdateView):
    template_name = "producto/form_producto.html"
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('producto_app:producto-lista')



class ProductDeleteView(AlmacenPermisoMixin, DeleteView):
    template_name = "producto/delete.html"
    model = Product
    success_url = reverse_lazy('producto_app:producto-lista')


class ProductDetailView(AlmacenPermisoMixin, DetailView):
    template_name = "producto/detail.html"
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #
        context["ventas_mes"] = SaleDetail.objects.ventas_mes_producto(
            self.kwargs['pk']
        )
        return context

'''