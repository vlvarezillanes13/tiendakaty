from django.urls import path
from . import views


app_name = 'productos'
urlpatterns = [
    path(
        'lista-de-productos',
        views.ProductoListView.as_view(),
        name='listar-productos'
    ),
    path(
        'detalle-del-producto/<pk>/',
        views.ProductoDetailView.as_view(),
        name='detalle-producto'
    ),
    
]