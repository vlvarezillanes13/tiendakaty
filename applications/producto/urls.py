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
    path(
        'agregar-producto/',
        views.ProductoCreateView.as_view(),
        name='agregar-producto'
    ),
    path(
        'eliminar-producto/<pk>/',
        views.ProductoDeleteView.as_view(),
        name='eliminar-producto'
    ),
    path(
        'actualizar-producto/<pk>/',
        views.ProductoUpdateView.as_view(),
        name='actualizar-producto'
    ),
]