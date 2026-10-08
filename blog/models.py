from django.db import models

# Create your models here.

class Entrada(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='blog/')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    entrada = models.ForeignKey(Entrada, on_delete=models.CASCADE, related_name='comentarios')
    nombre = models.CharField(max_length=100)
    texto = models.TextField(max_length=2000)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['fecha_creacion']

    def __str__(self):
        return f'{self.nombre}: {self.texto[:50]}'
