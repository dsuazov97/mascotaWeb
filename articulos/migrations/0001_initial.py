# Generated by Django 4.2.1 on 2023-06-13 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('idMarca', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Marca')),
                ('nombreMarca', models.CharField(blank=True, max_length=50, verbose_name='Marca')),
            ],
        ),
        migrations.CreateModel(
            name='TipoMascota',
            fields=[
                ('idMasc', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id TipoMasc')),
                ('nombreTipo', models.CharField(blank=True, max_length=50, verbose_name='Tipo de Mascota')),
            ],
        ),

        migrations.CreateModel(
            name='Alimento',
            fields=[
                ('cod', models.IntegerField(primary_key=True, serialize=False, verbose_name='Codigo')),
                ('nombre', models.CharField(blank=True, max_length=50, verbose_name='Nombre')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articulos.marca', verbose_name='Marca')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articulos.tipomascota', verbose_name='Tipo de Mascota')),
            ],
        ),
    ]