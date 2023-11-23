# En mi_app/views.py

from django.shortcuts import render
from .models import Curso, Alumno
from django.shortcuts import render, redirect
from .forms import CursoForm




def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'mi_app/cursos.html', {'cursos': cursos})



def detalle_curso(request, curso_id):
    curso = Curso.objects.get(pk=curso_id)
    return render(request, 'mi_app/detalle_curso.html', {'curso': curso})



def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'mi_app/alumnos.html', {'alumnos': alumnos})




def agregar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cursos')  # Redirige a la página que muestra la lista de cursos
    else:
        form = CursoForm()

    return render(request, 'agregar_curso.html', {'form': form})

# Repite el proceso para las otras vistas (agregar_detalle_curso y agregar_alumno)

