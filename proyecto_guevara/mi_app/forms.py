from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'  # Puedes especificar los campos que deseas incluir en el formulario

# Repite el proceso para los otros modelos (DetalleCurso y Alumno)
