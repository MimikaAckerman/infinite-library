from django.urls import path
from libros import views



app_name = 'libros'

urlpatterns = [
    path('', views.lista_libros, name='lista_libros'),
    path('buscar/', views.buscar_libro, name='buscar_libros'),
    path('libro/<int:libro_id>/', views.detalle_libro, name='detalle_libro'),
    path('subir/', views.subir_libro, name='subir_libro'),
    path('descargar/<int:libro_id>/', views.descargar_libro, name='descargar_libro'),
    path('eliminar/<int:libro_id>/', views.eliminar_libro, name='eliminar_libro'),
    path('editar/<int:libro_id>/', views.editar_libro, name='editar_libro'),

]
