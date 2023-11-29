from django import forms
from .models import Curso




class CrearCursoForm(forms.Form):
    nombre = forms.CharField(label='Nombre del Curso', max_length=100)
    descripcion = forms.CharField(label='Descripción', widget=forms.Textarea)
    precio = forms.DecimalField(label='Precio', min_value=0)


   
        
class BuscarCursoForm(forms.Form):
    nombre_curso = forms.CharField(max_length=255, required=False)