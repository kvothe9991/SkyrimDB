from django import forms
from django.db import models
from django.db.models import Count
from .models import Batalla, Hechizo, Participante

class GlobalObjectsForm(forms.Form):

    # OBJECT-WITH-SORT CHOICES:
    HECHIZO = 'HEC'
    HECHIZO_USADOS = 'HEC_QTY'
    BATALLAS = 'BAT'
    BATALLAS_DURAC = 'BAT_DUT'
    PARTICIPANTES = 'PAR'
    PARTICIPANTES_DMG = 'PAR_DMG'
    PARTICIPANTES_BAT = 'PAR_BTL'
    CHOICES = [ 
        (HECHIZO, 'Hechizos ordenados por nombre'),
        (HECHIZO_USADOS, 'Hechizos ordenados por cantidad de veces usados'),
        (BATALLAS, 'Batallas ordenadas por fecha'),
        (BATALLAS_DURAC, 'Batallas ordenadas por duración'),
        (PARTICIPANTES, 'Participantes ordenados por tipo'),
        (PARTICIPANTES_DMG, 'Participantes ordenados por daño realizado'),
        (PARTICIPANTES_BAT, 'Participantes ordenados por cantidad de batallas ganadas')
    ]

    # ASCENDING/DESCENDING:
    ASCENDING = 'ASC'
    DESCENDING = 'DESC'
    ORDER_CHOICES = [(ASCENDING,'Ascendiente'), (DESCENDING,'Descendiente')]

    # FIELDS:
    selection = forms.ChoiceField(choices=CHOICES, label='Objeto seleccionado', required=True)
    order = forms.ChoiceField(choices=ORDER_CHOICES, label='Ordenar', widget=forms.RadioSelect)
    max_amount = forms.IntegerField(initial=10, max_value=25, label='Cantidad')

    # FIELD WIDGET OVERRIDING:
    selection.widget.attrs.update({'class':'form-select'})
    order.widget.attrs.update({'class':'form-check-input', 'type':'radio'})
    max_amount.widget.attrs.update({'type':'number', 'class':'form-control'})

    # LABELS:
    labels = {
        HECHIZO: ('Hechizos',), BATALLAS: ('Batallas',), PARTICIPANTES: ('Participantes',),
        HECHIZO_USADOS: ('Hechizos', 'Veces lanzado'),
        BATALLAS_DURAC: ('Batallas', 'Duración'),
        PARTICIPANTES_BAT: ('Participantes', 'Batallas ganadas'),
        PARTICIPANTES_DMG: ('Participantes', 'Daño realizado')
    }

    # ANNOTATION_DATA:
    type_associations = { HECHIZO: Hechizo, PARTICIPANTES: Participante, BATALLAS: Batalla }
    
    annotation_data = {
        HECHIZO_USADOS: ('eventos', models.Count),
        BATALLAS_DURAC: ('eventos__noE', models.Max),
        PARTICIPANTES_BAT: ('eventos_ganados', models.Count),
        PARTICIPANTES_DMG: ('eventos_ganados__hlanzado__puntosDH', models.Sum)
    }

    def __make_annotation__(self, items, underscore_path, function, order):
        return items.annotate(col=function(underscore_path)).order_by(order + 'col')

    def get_selection(self):
        selection, top = self.cleaned_data['selection'], self.cleaned_data['max_amount']
        order = '-' if self.cleaned_data['order'] == self.DESCENDING else ''

        split = selection.split('_')
        model = self.type_associations[split[0]]
        items = model.objects.all()

        if len(split) > 1:
            annotated = self.__make_annotation__(items, *self.annotation_data[selection], order)
            items = [ (i,i.col) for i in annotated ]
        else:
            items = [ (i,) for i in items ]
        
        return self.labels[selection], items[0:top]


class ObjectsFromBattleForm(forms.Form):

    # OBJECT-TYPE CHOICES:
    HECHIZO = 'HEC'
    PARTICIPANTE = 'PAR'
    ALLOWED_OBJECTS = [(HECHIZO, 'Hechizo'), (PARTICIPANTE, 'Participante')]

    # SORT-TYPE CHOICES:
    SORT_NONE = 'NON'
    SORT_DMG = 'DMG'
    SORT_USED_SPELL = 'SPL'
    SORT_BY = [
        (SORT_NONE, 'Ninguno'), (SORT_DMG, 'Daño'), (SORT_USED_SPELL, 'Hechizos mas lanzados')
    ]

    # FIELDS
    selected_battle = forms.ModelChoiceField(queryset=Batalla.objects.all(), required=True, label='Batalla:')
    selected_object = forms.ChoiceField(choices=ALLOWED_OBJECTS, label='Objeto', required=True)
    # sorted_object = forms.ChoiceField(choices=SORT_BY, label='Ordenar por', required=True)
    sorted_object = forms.ChoiceField(choices=SORT_BY, label='Ordenar por', required=True, widget=forms.RadioSelect)
    amount = forms.IntegerField(initial=10, max_value=25, label='Cantidad')

    # FIELDS' WIDGET OVERRIDING:
    selected_battle.widget.attrs.update({'class':'form-select', 'aria-label':'Batalla'})
    selected_object.widget.attrs.update({'class':'form-select'})
    # sorted_object.widget.attrs.update({'class':'form-select'})
    sorted_object.widget.attrs.update({'class':'form-check-input', 'type':'radio'})
    amount.widget.attrs.update({'type':'number', 'class':'form-control'})


    def get_selection(self):
        get = lambda L: tuple(self.cleaned_data[x] for x in L)
        battle, sort_option, selection = get(['selected_battle', 'sorted_object', 'selected_object']) 
        top = get(['amount'])[0]

        if selection == self.PARTICIPANTE:
            labels = ('Participantes',)
            items =  Participante.objects.filter(eventos_ganados__batalla=battle).union(
                     Participante.objects.filter(eventos_perdidos__batalla=battle))
            if sort_option == self.SORT_DMG:
                x = 'eventos_ganados__hlanzado__puntosDH'
                items = items.annotate(dmg=models.Sum(x)).order_by('-dmg')
                items = [ (i, i.dmg) for i in items ]
                labels = (label[0], 'Daño')
            else:
                items = [ (i,) for i in items ]

        elif selection == self.HECHIZO:
            labels = ('Hechizos',)
            items = Hechizo.objects.filter(eventos__batalla=battle)
            if sort_option == self.SORT_USED_SPELL:
                items = items.annotate(e_count=Count('eventos')).order_by('-e_count')
                items = [ (i, i.e_count) for i in items ]
                labels = (labels[0], 'Veces lanzado')
            else:
                items = [ (i,) for i in items ]
        else:
            raise ValueError(f'Fue provisto {selection} de tipo {type(selection)} en formato inesperado.')
        
        return labels, items



class BattleForm(forms.ModelForm):
    
    class Meta:
        model = Batalla
        fields = '__all__'
