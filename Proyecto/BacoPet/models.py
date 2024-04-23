from django.db import models

class AdopcionPerro(models.Model):
    nombre_completo = models.CharField(max_length=100)
    correo_electronico = models.EmailField()
    telefono = models.IntegerField(max_length=20)
    tipo_vivienda = models.CharField(max_length=100)
    seguridad = models.TextField()
    personas_conviven = models.IntegerField()
    hijos = models.BooleanField()
    otras_mascotas = models.BooleanField()
    carnet_vacunacion_al_dia = models.BooleanField()
    relacion_con_otros_animales = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    completado = models.BooleanField(default=False)
    def __str__(self):
        return self.nombre_completo

class AdopcionGato(models.Model):
    nombre_completo = models.CharField(max_length=100)
    correo_electronico = models.EmailField()
    telefono = models.IntegerField(max_length=20)
    tipo_vivienda = models.CharField(max_length=100)
    seguridad = models.TextField()
    personas_conviven = models.IntegerField()
    hijos = models.BooleanField()
    otras_mascotas = models.BooleanField()
    carnet_vacunacion_al_dia = models.BooleanField()
    relacion_con_otros_animales = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    completado = models.BooleanField(default=False)
    def __str__(self):
        return self.nombre_completo


class QuieroSerPatrocinador(models.Model):
    nombre_completo = models.CharField(max_length=100)
    correo_electronico = models.EmailField()
    telefono = models.IntegerField(max_length=20)
    nombre_empresa = models.CharField(max_length=100)
    tipo_patrocinio = models.CharField(max_length=100)
    mensaje = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    completado = models.BooleanField(default=False)
    def __str__(self):
        return self.nombre_completo

class Persona(models.Model):
    nombre_completo = models.CharField(max_length=100)
    esta_en_adopcion = models.BooleanField(default=False)
    esta_patrocinada = models.BooleanField(default=False)
    completo_formulario_adopcion_perro = models.BooleanField(default=False)
    completo_formulario_adopcion_gato = models.BooleanField(default=False)
    completo_formulario_patrocinador = models.BooleanField(default=False)

    @classmethod
    def buscar_persona(cls, nombre):
        return cls.objects.filter(nombre__icontains=nombre)
