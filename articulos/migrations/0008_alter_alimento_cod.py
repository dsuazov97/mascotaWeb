# Generated by Django 4.2.1 on 2023-07-12 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0007_boleta_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alimento',
            name='cod',
            field=models.CharField(max_length=5, primary_key=True, serialize=False, verbose_name='Codigo'),
        ),
    ]
