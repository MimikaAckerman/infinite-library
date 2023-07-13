from django.urls import path
from . import views

from .views import subir_libro

app_name = 'libros'

urlpatterns = [
    path('', views.lista_libros, name='lista_libros'),
    path('buscar/', views.buscar_libro, name='buscar_libros'),
    path('libro/<int:libro_id>/', views.detalle_libro, name='detalle_libro'),
    path('subir/', subir_libro, name='subir_libro'),
    path('descargar/<int:libro_id>/', views.descargar_libro, name='descargar_libro'),
    path('eliminar/',views.eliminar_libro, name='eliminar_libro'),
]
