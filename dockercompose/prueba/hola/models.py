from django.db import models


class Hola(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    correo = models.EmailField()
    telefono = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre
