from applications.producto.models import Producto
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    TemplateView,
)
# Create your views here.


class HomePageView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView,self).get_context_data(**kwargs)
        # productos
        context['productos'] = Producto.objects.all()
        return context