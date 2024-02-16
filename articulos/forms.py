#es una clase que tiene la información que llevará uno o  más formularios en un template
from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Alimento,Marca,TipoMascota
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class RegistroUserForm(UserCreationForm):
    class Meta: 
        model=User 
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class AlimentoForm(forms.ModelForm):
    class Meta:
        model = Alimento 
        fields = ['cod', 'nombre', 'tipo', 'marca','imagen','precio','stock']
        labels = {
            'cod' : "Codigo",
            'nombre' : "Nombre",
            'tipo' : "Tipo",
            'marca' : "Marca",
            'imagen' : 'Imagen',
            'precio': "Precio",
            'stock': "Stock"
        }
        widgets={
            'cod' : forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese codigo',
                    'class' : 'form-control',
                    'id' : 'cod'
                }
            ),
            'nombre':forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese nombre',
                    'class' : 'form-control',
                    'id' : 'nombre'
                }
            ),
            'tipo':forms.Select(
                attrs={
                    'class' : 'form-control',
                    'id' : 'tipo'
                }
            ),
            'marca':forms.Select(
                attrs={
                    'class' : 'form-control',
                    'id' : 'marca'
                }
            ),
            'imagen':forms.FileInput(
                attrs={
                    'class' : 'form-control',
                    'id' : 'imagen'
                }
            ),
            'precio':forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese valor',
                    'class' : 'form-control',
                    'id' : 'precio'
                }
            ),
            'stock':forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese Stock',
                    'class' : 'form-control',
                    'id' : 'stock'
                }
            )
        }