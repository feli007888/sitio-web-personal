from django.shortcuts import get_object_or_404, redirect, render
from .forms import ComentarioForm
from .models import Entrada

# Create your views here.

def blog(request):
    entradas = Entrada.objects.order_by('-fecha_publicacion')
    return render(request, 'blog.html', {'entradas': entradas})


def detalle_entrada(request, entrada_id):
    entrada = get_object_or_404(Entrada, pk=entrada_id)
    if request.method == 'POST':
        formulario = ComentarioForm(request.POST)
        if formulario.is_valid():
            comentario = formulario.save(commit=False)
            comentario.entrada = entrada
            comentario.save()
            return redirect('detalle_entrada', entrada_id=entrada.pk)
    else:
        formulario = ComentarioForm()

    return render(request, 'blog/entrada_detalle.html', {
        'entrada': entrada,
        'comentarios': entrada.comentarios.all(),
        'formulario': formulario,
    })
