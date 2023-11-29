# En mi_app/views.py
from .models import Curso, Alumno
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import CrearCursoForm, BuscarCursoForm




def lista_cursos(request):
    cursos = Curso.objects.all()
    contexto = {
        "cursos": cursos,
        "nombre": "Placeholder",
        "form":BuscarCursoForm
            }
    return render(request, "cursos.html",contexto)



def detalle_curso(request, curso_id):
    curso = Curso.objects.get(pk=curso_id)
    return render(request, 'detalle_curso.html', {'curso': curso})



def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'alumnos.html', {'alumnos': alumnos})



def mis_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos.html', {'cursos': cursos})




def crear_curso(request):
    curso= Curso(nombre="Python", descripcion="texto de prueba")
    curso.save()
    
    return redirect("/cursos")


def crear_curso_form(request):
    
    if request.method == "POST":
        #crear curso
        curso_formulario = CrearCursoForm(request.POST)
        if curso_formulario.is_valid():
            informacion = curso_formulario.cleaned_data
            
            curso_crear = Curso(nombre = informacion["nombre"], descripcion = informacion["descripcion"])
            curso_crear.save()
            return redirect("/mi_app/home")
            
    curso_formulario = CrearCursoForm()
    contexto = {
        "form": curso_formulario
        
    }
    return render(request, "crear_curso.html",contexto)


def home(request):
    return render(request, 'home.html')

"""
def busqueda(request):
    nombre = request.GET["nombre"]
    cursos = Curso.objects.filter(nombre__icontains=nombre)
    contexto = {
        "cursos": cursos,
        "nombre": "Placeholder",
        "form":BuscarCursoForm(),
            }
    return render(request, "/mi_app/cursos", contexto)
"""
    
def buscar_curso(request):
    form = BuscarCursoForm(request.GET or None)
    cursos_encontrados = []

    if request.method == 'GET' and form.is_valid():
        nombre_curso = form.cleaned_data['nombre_curso']
        cursos_encontrados = Curso.objects.filter(nombre__icontains=nombre_curso)

    return render(request, 'buscar_curso_resultados.html', {'form': form, 'cursos_encontrados': cursos_encontrados})