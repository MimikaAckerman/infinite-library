from django.test import TestCase
from django.urls import reverse
from .models import Libro


from django.core.files.uploadedfile import SimpleUploadedFile




#visualizar libro
class Visualizar_libroTestCase(TestCase):
    def setUp(self):
        self.libro1 = Libro.objects.create(titulo='Libro 1', autor='Autor 1', descripcion='Descripción 1')
        self.libro2 = Libro.objects.create(titulo='Libro 2', autor='Autor 2', descripcion='Descripción 2')
    def test_lista_libros(self):
        response = self.client.get(reverse('libros:lista_libros'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'libros/lista_libros.html')
        self.assertContains(response, self.libro1.titulo)
        self.assertContains(response, self.libro2.titulo)


#eliminar libro
class Eliminar_libroTestCase(TestCase):
    def setUp(self):
        self.libro = Libro.objects.create(titulo='Libro 1', autor='Autor 1', descripcion='Descripción 1')
        
    def test_eliminar_libro(self):
        response = self.client.post(reverse('libros:eliminar_libro',args=[self.libro.id]))
        self.assertEqual(response.status_code,302)
        self.assertRedirects(response,reverse('libros:lista_libros'))
        self.assertFalse(Libro.objects.filter(pk=self.libro.id).exists())
        

#subir libro
class SubirLibroTestCase(TestCase):
    def test_subir_libro(self):
        url = reverse('libros:subir_libro')
        archivo_pdf = SimpleUploadedFile("test_file.pdf", b"pdf_content", content_type="application/pdf")

        data = {
            'titulo': 'Título del libro',
            'autor': 'Autor del libro',
            'descripcion': 'Descripción del libro',
        }
        files = {
            'archivo_pdf': archivo_pdf,
        }
        response = self.client.post(url, data=data, files=files)

        self.assertEqual(response.status_code, 302)  # Se espera una redirección
        self.assertEqual(Libro.objects.count(), 1)  # Se espera que se haya creado un libro
        libro = Libro.objects.first()
        self.assertEqual(libro.titulo, 'Título del libro')  # Se espera que el título sea correcto
        self.assertEqual(libro.autor, 'Autor del libro')  # Se espera que el autor sea correcto
        self.assertEqual(libro.descripcion, 'Descripción del libro')  # Se espera que la descripción sea correcta
        self.assertEqual(libro.archivo_pdf.name, 'pdfs/test_file.pdf')  # Se espera que el nombre del archivo PDF sea correcto

    


#buscar libro 

    
#descargar libro 

#editar libro

