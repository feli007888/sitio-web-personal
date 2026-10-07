from django.shortcuts import get_object_or_404, render
from .models import Entrada

# Create your views here.

def blog(request):
    entradas = Entrada.objects.order_by('-fecha_publicacion')
    return render(request, 'blog.html', {'entradas': entradas})


def detalle_entrada(request, entrada_id):
    entrada = get_object_or_404(Entrada, pk=entrada_id)
    return render(request, 'blog/entrada_detalle.html', {'entrada': entrada})
