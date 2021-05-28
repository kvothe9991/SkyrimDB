from django.contrib import admin
from .models import Participante, Evento, Hechizo, Batalla, TipoDD, Jugador, Personaje, Bestia

# Register your models here.
admin.site.register(Evento)
admin.site.register(Hechizo)
admin.site.register(Batalla)
admin.site.register(TipoDD)
admin.site.register(Jugador)
admin.site.register(Personaje)
admin.site.register(Bestia)
admin.site.register(Participante)