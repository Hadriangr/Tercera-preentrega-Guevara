from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    camada = models.IntegerField(unique=True)