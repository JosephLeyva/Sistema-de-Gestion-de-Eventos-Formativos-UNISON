from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import *

class CrearFormularioUsuario(UserCreationForm):
	class Meta:
            model = User
            fields = ['name', 'username', 'email', 'password1', 'password2']