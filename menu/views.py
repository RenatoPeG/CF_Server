from .models import Personaje
from django.shortcuts import render
from django.http import Http404


def menu(request):
    personajes = Personaje.objects.all()
    return render(request, 'menu/menu.html', {'personajes': personajes})


def detalle(request, personaje_id):
    try:
        personaje = Personaje.objects.get(pk=personaje_id)
    except Personaje.DoesNotExist:
        raise Http404('Personaje no existe')
    return render(request, 'menu/detalle.html', {'personaje': personaje})


def seleccion_personaje(request):
    personajes = Personaje.objects.all()
    return render(request, 'menu/seleccion_personaje.html', {'personajes': personajes})
