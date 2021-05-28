from django.db import models
from django.db.models import CASCADE

class AutoFieldNonPrimary(models.AutoField):
        def _check_primary_key(self):
            if self.primary_key:
                return [
                    models.fields.checks.Error(
                        'AutoFieldNonPrimary must not set primary_key=True.',
                        obj=self, id='fields.E100',)]
            else:
                return []


class Personaje(models.Model):

    idP = models.AutoField(primary_key=True, verbose_name='ID') #tiene restricción de unicidad
    nombreP = models.CharField(max_length=200, verbose_name='Nombre')
    razaP = models.CharField(max_length=200, verbose_name='Raza')
    puntosSaludP = models.IntegerField()

    class Meta:
        ordering = ["nombreP"]

    def __str__(self):
        return self.nombreP


class Hechizo(models.Model):

    nombreH = models.CharField(verbose_name='Nombre', primary_key=True, max_length=200) #tiene restricción de unicidad
    puntosDH = models.IntegerField(verbose_name='Puntos de Daño')

    class Meta:
        ordering = ["nombreH"]

    def __str__(self):
        return self.nombreH


class TipoDD(models.Model):
    
    nombreD = models.CharField(primary_key=True, max_length=200) #tiene restricción de unicidad

    class Meta:
        ordering = ["nombreD"]
        verbose_name = 'Tipo de Daño'
        verbose_name_plural = 'Tipos de Daño'

    def __str__(self):
        return self.nombreD


class Participante(models.Model):

    idPar = models.AutoField(primary_key=True, verbose_name='ID') #tiene restricción de unicidad
    deb = models.ForeignKey(TipoDD, CASCADE,
        related_name="%(class)s_deb", verbose_name='Debilidad') #daño al que es débil
    inf = models.ForeignKey(TipoDD, CASCADE,
        related_name="%(class)s_inf", verbose_name='Daño') #daño que inflige 

    def __get_name__(self):
        if hasattr(self, 'bestia'):
            return self.bestia.nombreB
        elif hasattr(self, 'jugador'):
            return self.jugador.personaje.nombreP
        else:
            raise ValueError('No debería haber un participante que no es de tipo de alguno de sus hijos...')

    def __str__(self):
        return f"{self.__get_name__()}"


class Batalla(models.Model):

    idBat = models.AutoField(primary_key=True) #tiene restricción de unicidad
    lugar = models.CharField(max_length=200)
    sobreviviente = models.ForeignKey(Participante, CASCADE, related_name='sobreviviente')
    fecha = models.DateTimeField()

    class Meta:
        ordering = ["fecha"]

    def __str__(self):
        return f'{self.lugar} - {str(self.fecha)}'

    def duration(self):
        return self.evento_set.count()


class Bestia(Participante):

    participante = models.OneToOneField(Participante, CASCADE, primary_key=True, related_name="%(class)s", parent_link=True) #tiene restricción de unicidad
    nombreB = models.CharField(max_length=200, verbose_name='Nombre')
    razaB = models.CharField(max_length=200, verbose_name='Raza')
    puntosDB = models.IntegerField(verbose_name='Daño')
    puntosSB = models.IntegerField(verbose_name='Salud')

    class Meta:
        ordering = ["nombreB"]

    def __str__(self):
        return self.nombreB


class Jugador(Participante):
    participante = models.OneToOneField(Participante, CASCADE, related_name="%(class)s", parent_link=True) #tiene restricción de unicidad
    personaje = models.OneToOneField(Personaje, CASCADE, related_name="%(class)s") #tiene restricción de unicidad
    hechizo = models.ForeignKey(Hechizo, CASCADE, related_name='%(class)s')

    class Meta:
        ordering = ["participante"]
        unique_together = (("participante", "personaje", "hechizo"),)
        verbose_name_plural = 'Jugadores'

    def __str__(self):
        return self.personaje.nombreP


class Evento(models.Model):
    atacante = models.ForeignKey(
        Participante, CASCADE, related_name="eventos_ganados", verbose_name='Atacante')
    damnificado = models.ForeignKey(
        Participante, CASCADE, related_name="eventos_perdidos", verbose_name='Damnificado') 
    batalla = models.ForeignKey(Batalla, CASCADE, related_name="eventos", verbose_name='Batalla') #tiene restricción de unicidad
    hlanzado = models.ForeignKey(Hechizo, CASCADE, related_name="eventos", verbose_name='Hechizo Lanzado')
    saludDA = models.IntegerField(verbose_name='Salud del Atacante')
    noE = models.IntegerField(verbose_name='Número de Evento')
    
    def __str__(self):
        return f"Evento #{self.noE} - {self.batalla.lugar}"

    class Meta:
        ordering = ["batalla"]
        unique_together = (("atacante", "damnificado", "batalla"))