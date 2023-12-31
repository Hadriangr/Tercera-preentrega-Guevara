# En mi_app/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('home/',views.home, name='inicio'),
    path('cursos/', views.lista_cursos, name='lista_cursos'),
    path('alumnos/', views.lista_alumnos, name='lista_alumnos'),
    path('crear_curso/', views.crear_curso_form, name='crear_curso'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('mis_cursos/', views.mis_cursos, name='mis_cursos'),
    #path('buscar/', views.busqueda, name='buscar'),
    path('buscar_curso/', views.buscar_curso, name='buscar_curso'),
    
]

