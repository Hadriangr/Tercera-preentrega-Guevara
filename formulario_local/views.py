from forms import CursoForm,BusquedaCursoForm
from  django.shortcuts import render,redirect
from models import Curso


def mostrar_cursos(request):
    cursos = Curso.objects.all()
    contexto = {
        "cursos": cursos,
        "nombre": "Placeholder",
        "form":BusquedaCursoForm
            }
    return render(request, "/cursos.html",contexto)



def crear_curso(request):
    curso= Curso(nombre="Python", camada="3443")
    curso.save()
    
    return redirect("/cursos")


def crear_curso_form(request):
    
    if request.method == "POST":
        #crear curso
        curso_formulario = CursoForm(request.POST)
        if curso_formulario.is_valid():
            informacion = curso_formulario.cleaned_data
            
            curso_crear = Curso(nombre = informacion["nombre"], camada = informacion["camada"])
            curso_crear.save()
            return redirect("/cursos")
            
    curso_formulario = CursoForm()
    contexto = {
        "form": curso_formulario
        
    }
    return render(request, "crear_curso.html",contexto)


def busqueda_camada(request):
    nombre = request.GET["nombre"]
    cursos = Curso.objects.filter(nombre__icontains=nombre)
    contexto = {
        "cursos": cursos,
        "nombre": "Placeholder",
        "form":BusquedaCursoForm
            }
    return render(request, "/cursos.html", contexto)