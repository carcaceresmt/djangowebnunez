from django.db import models

# Create your models here.
class Persona(models.Model):

    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    direccion=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
