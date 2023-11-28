from django import forms
from .models import Curso
from django.contrib.auth.forms import UserCreationForm

"""
class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'  



class CustomUserCreationForm(UserCreationForm):
    error_messages = {
        'password_mismatch': 'Las contraseñas no coinciden.',
        'password_too_short': 'La contraseña es demasiado corta. Debe contener al menos 8 caracteres.',
        'password_common': 'Esta contraseña es demasiado común.',
        'password_numeric': 'La contraseña no puede ser completamente numérica.',
        # Puedes agregar otros mensajes según tus necesidades
    }

    username = forms.CharField(label='Nombre de usuario')
    password1 = forms.CharField(
        label='Contraseña\n',
        widget=forms.PasswordInput,
        help_text="Tu contraseña no puede ser demasiado similar a tu otra información personal\n"
                     "Debe contener al menos 8 caracteres. \n No puede ser una contraseña común ni completamente numérica."
    )
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput,
        help_text='Ingresa la misma contraseña para su verificación.'
    )
"""



class CrearCursoForm(forms.Form):
    nombre = forms.CharField(label='Nombre del Curso', max_length=100)
    descripcion = forms.CharField(label='Descripción', widget=forms.Textarea)
    precio = forms.DecimalField(label='Precio', min_value=0)


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'descripcion']
   
        
class BuscarCursoForm(forms.Form):
    nombre_curso = forms.CharField(max_length=255, required=False)