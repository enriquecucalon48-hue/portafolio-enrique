from django.shortcuts import render


def inicio(request):
    return render(request, 'inicio.html')


def sobre_mi(request):
    return render(request, 'sobre_mi.html')


def proyectos(request):
    return render(request, 'proyectos.html')


def proyecto_detalle(request):
    return render(request, 'proyecto_detalle.html')


def contacto(request):
    return render(request, 'contacto.html')
