from django.contrib import admin
from .models import Alimento,Marca,TipoMascota,Boleta,detalle_boleta

# Register your models here.

admin.site.register(Alimento)
admin.site.register(Marca)
admin.site.register(TipoMascota)
admin.site.register(detalle_boleta)
admin.site.register(Boleta)

