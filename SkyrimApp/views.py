from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import ObjectsFromBattleForm, GlobalObjectsForm
from . models import Participante, Evento, Hechizo

# Create your views here.
"""
Requerimientos funcionales:
``````````````````````````
• Insertar nuevos Jugadores, Bestias, Hechizos, y modificar información sobre estos.
• Registrar nuevas Batallas.
• Obtener información sobre Participantes o Batallas en dependencia de
restricciones o condiciones determinadas.


Requerimientos Informacionales:
``````````````````````````````
• Conocer los Participantes de determinada Batalla.
• Conocer los hechizos más(menos) usados en una Batalla o globalmente.
• Saber sobre Batallas más(menos) duraderas (cantidad de eventos en la
Batalla).
• Conocer sobre los Participantes que han ganado más batallas.
• Conocer sobre los participantes que han ocasionado más(menos) daño en
una Batalla o globalmente.
"""

def home(request):
    return render(request, 'SkyrimApp/home.html', context={})

FORM_TYPES = { 
    'battle': ObjectsFromBattleForm,
    'global': GlobalObjectsForm
}

@csrf_exempt
def visualize_data(request, form_type):
    form_t = FORM_TYPES[form_type]
    if request.method == 'POST':
        form = form_t(request.POST)
        if form.is_valid():
            labels,items = form.get_selection()
            context = { 'form':form, 'labels':labels, 'items':items }
        else:
            return HttpResponse('Invalid form')
    else:
        form = form_t()
        context = { 'form':form, 'items':None }
    return render(request, f'SkyrimApp/{form_type}.html', context=context)
