# En mi_app/views.py
from .models import Curso, Alumno
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import CrearCursoForm,CursoForm




def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos.html', {'cursos': cursos})



def detalle_curso(request, curso_id):
    curso = Curso.objects.get(pk=curso_id)
    return render(request, 'detalle_curso.html', {'curso': curso})



def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'alumnos.html', {'alumnos': alumnos})



def mis_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'mis_cursos.html', {'cursos': cursos})




def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mis_cursos')
    else:
        form = CursoForm()

    return render(request, 'crear_curso.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # ... resto del código para el registro exitoso
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})


def home(request):
    return render(request, 'home.html')