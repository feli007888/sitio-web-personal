from django.db import models

# Create your models here.

class Entrada(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='blog/')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)