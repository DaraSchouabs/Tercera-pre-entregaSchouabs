from django.contrib import admin
from BacoPet.models import AdopcionPerro, AdopcionGato, QuieroSerPatrocinador

# Registra tus modelos aquí
admin.site.register(AdopcionPerro)
admin.site.register(AdopcionGato)
admin.site.register(QuieroSerPatrocinador)
