from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .forms import CrearFormularioUsuario

# Create your views here.


'''
def PaginaLogin(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'El Usuario o la contraseña son incorrectos')

	context = {}
	return render(request, 'login.html', context)

'''
def inicio(request):
	context = {}

	return render(request, 'inicio.html', context)