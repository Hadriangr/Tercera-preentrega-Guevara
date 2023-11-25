from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Catedra(models.Model):
    nombre = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    profesor = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.curso}"

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    catedras = models.ManyToManyField(Catedra)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.curso}"
