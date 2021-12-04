from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import *


class CrearUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['first_name','last_name','username','email','password1','password2','rol']


class UserForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['first_name','last_name','email','imagen']


class DateInput(forms.DateInput):
    input_type = 'date'


class EventoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EventoForm, self).__init__(*args, **kwargs)
        self.fields['responsable'].widget.attrs['hidden'] = True 
    class Meta:
        model = Evento
        fields = '__all__'
        widgets = {
            'Fecha_de_Inicio': DateInput(attrs={'type': 'date'}),
            'Fecha_de_Fin': DateInput(attrs={'type': 'date'}),
        }

