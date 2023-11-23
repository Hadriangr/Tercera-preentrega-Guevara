# En mi_app/urls.py

from django.urls import path
from . import views
from .views import agregar_curso

urlpatterns = [
    path('cursos/', views.lista_cursos, name='lista_cursos'),
    path('cursos/<int:curso_id>/', views.detalle_curso, name='detalle_curso'),
    path('alumnos/', views.lista_alumnos, name='lista_alumnos'),
    path('agregar_curso/', agregar_curso, name='agregar_curso'),
]

