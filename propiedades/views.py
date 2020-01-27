from django.shortcuts import render

from django.shortcuts import render
from propiedades.models import Propiedad


def propiedad_index(request):
    propiedades = Propiedad.objects.all()
    context = {
        'propiedades': propiedades
    }
    return render(request, 'propiedad_index.html', context)


def propiedad_detail(request, pk):
    propiedad = Propiedad.objects.get(pk=pk)
    context = {
        'propiedad': propiedad
    }
    return render(request, 'propiedad_detail.html', context)

