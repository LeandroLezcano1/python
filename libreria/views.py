from django.shortcuts import render
from django.http import HttpResponse
from .models import equipo
from .forms import equipoform
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def about_me(request):
    return render(request, 'paginas/about_me.html')

def equipos(request):
    equipos = equipo.objects.all()
    return render(request, 'equipos/index.html', {'equipos': equipos})

def login(request):
    return render(request, 'paginas/login.html')

def signup(request):
    return render(request, 'paginas/signup.html')

def crear(request):
    formulario = equipoform(request.POST or None)
    return render(request, 'equipos/crear.html', {formulario: formulario})

def editar(request):
    return render(request, 'equipos/editar.html')
