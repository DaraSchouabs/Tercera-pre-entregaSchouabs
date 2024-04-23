from django.urls import path
from BacoPet import views
from BacoPet.views import buscar_resultados

urlpatterns = [

    path('adopcion_perro/', views.adopcion_perro, name='adopcion_perro'),
    path('adopcion_gato/', views.adopcion_gato, name='adopcion_gato'),
    path('ser_patrocinador/', views.ser_patrocinador, name='ser_patrocinador'),
    path('gracias/', views.gracias, name='gracias'),
    path('buscar/', buscar_resultados, name='buscar_resultados')
]
