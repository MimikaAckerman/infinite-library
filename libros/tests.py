from django.test import TestCase, RequestFactory
from django.urls import reverse

from .models import Libro
from .views import subir_libro, buscar_libro
from django.core.files.uploadedfile import SimpleUploadedFile


class SubirLibroTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_subir_libro(self):
        url = reverse('libros:subir_libro')
        data = {
            'titulo': 'Nuevo título',
            'autor': 'Nuevo autor',
            'description': 'Nueva descripción',
           
        }
        archivo_pdf = SimpleUploadedFile(
            "archivo.pdf",
            b"contenido_pdf",
            content_type="application/pdf"  # Especifica el tipo de contenido del archivo
        )
        
        files = {'archivo_pdf': archivo_pdf}
        request = self.factory.post(url, data=data, files=files)

        response = subir_libro(request)
        self.assertEqual(response.status_code, 200)

        libros = Libro.objects.all()
        self.assertEqual(len(libros), 1)
        nuevo_libro = libros.first()
        self.assertEqual(nuevo_libro.titulo, 'Nuevo título')
        self.assertEqual(nuevo_libro.autor, 'Nuevo autor')
        self.assertEqual(nuevo_libro.description, 'Nueva descripción')
        

# class BuscarLibroTestCase(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()

#         Libro.objects.create(titulo='Libro A', autor='Autor A', descripcion='Descripción A')
#         Libro.objects.create(titulo='Libro B', autor='Autor B', descripcion='Descripción B')
#         Libro.objects.create(titulo='Libro C', autor='Autor C', descripcion='Descripción C')

#     def test_buscar_libro(self):
#         url = reverse('libros:buscar_libros')
#         query = 'Libro A'
#         request = self.factory.get(url, data={'q': query})

#         response = buscar_libro(request)

#         self.assertEqual(response.status_code, 200)

#         libros = response.context['libros']
#         self.assertEqual(len(libros), 1)

#         libro_encontrado = libros[0]
#         self.assertEqual(libro_encontrado.titulo, 'Libro A')
#         self.assertEqual(libro_encontrado.autor, 'Autor A')
#         self.assertEqual(libro_encontrado.descripcion, 'Descripción A')
