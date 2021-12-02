from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Evento
from .forms import EventoForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Usuario no existe')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username o password no existe')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('/')

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Error en el registro')

    return render(request, 'base/login_register.html', {'form':form})

def Home(request):
    context = {}
    return render(request,'base/home.html', context)

def PropuestasEventosFormativos(request):
    eventosformativos = Evento.objects.all()
    propuesta_count = eventosformativos.count()
    context = {'eventosformativos':eventosformativos, 'propuesta_count':propuesta_count}
    return render(request,'base/PropuestasEventosFormativos.html', context)

def Propuesta(request,pk):
    evento = Evento.objects.get(id=pk)
    context = {'evento':evento}
    return render(request,'base/Propuesta.html', context)

@login_required(login_url='/')
def createPropuesta(request):
    form = EventoForm()
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('PropuestasEventosFormativos')

    context = {'form': form}
    return render(request,'base/Propuesta_form.html', context)

@login_required(login_url='/')
def updatePropuesta(request, pk):
    evento = Evento.objects.get(id=pk)
    form = EventoForm(instance=evento)

    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('PropuestasEventosFormativos')
    context = {'form': form}
    return render(request,'base/Propuesta_form.html', context)

@login_required(login_url='/')
def deletePropuesta(request, pk):
    evento = Evento.objects.get(id=pk)
    if request.method == 'POST':
        evento.delete()
        return redirect('PropuestasEventosFormativos')
    return render(request,'base/borrar.html', {'obj':evento})