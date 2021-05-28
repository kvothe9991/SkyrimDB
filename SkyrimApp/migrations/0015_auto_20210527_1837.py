# Generated by Django 3.1.7 on 2021-05-27 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SkyrimApp', '0014_bestia_jugador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jugador',
            name='id',
        ),
        migrations.AlterField(
            model_name='bestia',
            name='nombreB',
            field=models.CharField(max_length=200, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='bestia',
            name='participante',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='bestia', serialize=False, to='SkyrimApp.participante'),
        ),
        migrations.AlterField(
            model_name='bestia',
            name='puntosDB',
            field=models.IntegerField(verbose_name='Daño'),
        ),
        migrations.AlterField(
            model_name='bestia',
            name='puntosSB',
            field=models.IntegerField(verbose_name='Salud'),
        ),
        migrations.AlterField(
            model_name='bestia',
            name='razaB',
            field=models.CharField(max_length=200, verbose_name='Raza'),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='participante',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='jugador', serialize=False, to='SkyrimApp.participante'),
        ),
    ]
