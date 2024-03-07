from django.db import models

# Create your models here.
class Formulario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    asunto = models.CharField(max_length=200)
    mensaje = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.asunto}"