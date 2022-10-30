# from dataclasses import field
# from msilib.schema import Class
from django.db import models


# Create your models here.
class Curso(models.Model):

    nombre = models.CharField(max_length=50)
    camada = models.IntegerField()

    def __str__(self) -> str:
        return f"// Nombre: {self.nombre} // Camada: {self.camada}//"


class Estudiante(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()


class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)


class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
