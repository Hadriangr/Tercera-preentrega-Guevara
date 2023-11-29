from django import forms



class CursoForm(forms.Form):
    nombre = forms.CharField()
    camada = forms.integerField()
    
    
    
class BusquedaCursoForm(forms.Form):
    nombre = forms.CharField()    
    