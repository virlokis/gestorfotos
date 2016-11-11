from django.shortcuts import get_object_or_404, render

from .models import Evento, Foto, Dorsal


def index(request):
    latest_eventos_list = Evento.objects.order_by('-fecha')[:5]
    return render(request, 'gestorfotos/index.html', {
        'latest_eventos_list': latest_eventos_list
        }
    )


def evento(request, evento_id):
    fotos = Foto.objects.filter(dorsal__evento__id=evento_id)
    return render(request, 'gestorfotos/evento.html', {
        'fotos': fotos,
    })
