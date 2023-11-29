from django.urls import path
from views import crear_curso,mostrar_cursos,busqueda_camada,crear_curso_form

urlpatterns = [
    path('agregar_curso/', crear_curso),
    path('curso/', crear_curso_form),
    path('buscar/', busqueda_camada),
    path('cursos/', mostrar_cursos)
]
