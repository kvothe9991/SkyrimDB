# Generated by Django 3.1.7 on 2021-05-26 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SkyrimApp', '0003_auto_20210525_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='participante1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventos_par1', to='SkyrimApp.participante'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='participante2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventos_par2', to='SkyrimApp.participante'),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='hechizo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jugador', to='SkyrimApp.hechizo'),
        ),
    ]