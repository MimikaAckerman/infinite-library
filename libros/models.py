from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250, default='')
    #enneste campo se almacenaran los archivos pdf subidos por el usuario
    archivo_pdf = models.FileField(upload_to='pdfs/')
    #aqui se almacenara la fecha del libro publicado , indica la fecha automaticamente
    fecha_publicacion = models.DateField(auto_now_add=True)
    
    #este metodo define como se representara el libro , en este caso sera como cadena de texto
    def __str__(self):
        return self.titulo