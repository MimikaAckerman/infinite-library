from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Libro
from django.shortcuts import render, get_object_or_404, redirect


import time

from django.http import FileResponse



# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import FileResponse
from .models import Libro

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request ,'libros/lista_libros.html',{'libros':libros})



def detalle_libro(request,libro_id):
    libro = get_object_or_404(Libro,pk = libro_id)
    return render(request,'libros/detalle_libro.html',{'libro':libro})
    


def subir_libro(request):
    if request.method == 'POST':
        
        titulo = request.POST['titulo']
        autor = request.POST['autor']
        descripcion = request.POST['descripcion']
        print(request.FILES)
        archivo_pdf = request.FILES['archivo_pdf']
        
        libro = Libro(titulo=titulo, autor=autor, descripcion=descripcion, archivo_pdf=archivo_pdf)
        
        libro.save()
        time.sleep(2) #agregamos una pausa de 2 segundos
        return redirect('Libros:lista_libros')
    else:
          return render(request, 'libros/subir_libro.html')


def descargar_libro(request,libro_id):
    libro = get_object_or_404(Libro , pk=libro_id)
    archivo = libro.archivo_pdf
    response = FileResponse(archivo)
    response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(libro.titulo)
    return response

def buscar_libro(request):
    if request.method == 'POST':
        if 'q' in request.POST:
            query = request.POST['q']
            libros = Libro.objects.filter(titulo__icontains=query)
        else:
            libros = Libro.objects.all()
    else:
        libros = Libro.objects.all()
    return render(request, 'libros/lista_libros.html', {'libros': libros})


#funcion de editar y eliminar elemento
def eliminar_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    if request.method == 'POST':
        libro.delete()
        return redirect('libros:lista_libros')
    else:
        return render(request, 'libros/eliminar_libro.html', {'libro': libro})
    
    
def editar_libro(request,libro_id):
    libro = get_object_or_404(Libro,pk=libro_id)
    if request.method == 'POST':
        libro.titulo = request.POST['titulo']
        libro.autor = request.POST['autor']
        libro.descripcion = request.POST['descripcion']
        libro.save()
        
        return redirect('libros:lista_libros')
    else:
        return render(request,'libros/editar_libro.html',{'libro':libro})