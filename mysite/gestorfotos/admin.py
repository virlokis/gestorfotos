from django.contrib import admin

from .models import Evento, Competidor, Dorsal, Foto

admin.site.register(Evento)
admin.site.register(Competidor)
admin.site.register(Dorsal)
admin.site.register(Foto)