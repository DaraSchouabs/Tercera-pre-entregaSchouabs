from django.shortcuts import render, redirect
from BacoPet.models import AdopcionPerro, AdopcionGato, QuieroSerPatrocinador, Persona
from BacoPet.forms import AdopcionPerroForm, AdopcionGatoForm, QuieroSerPatrocinadorForm, BusquedaForm
from django.views import View

def adopcion_perro(request):
    if request.method == 'POST':
        form = AdopcionPerroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gracias')
    else:
        form = AdopcionPerroForm()
    return render(request, 'adopcion_perro.html', {'form': form})

def adopcion_gato(request):
    if request.method == 'POST':
        form = AdopcionGatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gracias')
    else:
        form = AdopcionGatoForm()
    return render(request, 'adopcion_gato.html', {'form': form})

def ser_patrocinador(request):
    if request.method == 'POST':
        form = QuieroSerPatrocinadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gracias')
    else:
        form = QuieroSerPatrocinadorForm()
    return render(request, 'ser_patrocinador.html', {'form': form})

def gracias(request):
    return render(request, 'gracias.html')

def base(request):
    titulo = 'Inicio - Mi Aplicación'
    contenido = 'Bienvenido a Mi Aplicación'
    return render(request, 'base.html', {'titulo': titulo, 'contenido': contenido})

def buscar_resultados(request):
    if 'nombre' in request.GET:
        nombre_busqueda = request.GET['nombre']
        resultados_perros = AdopcionPerro.objects.filter(nombre_completo__icontains=nombre_busqueda)
        resultados_gatos = AdopcionGato.objects.filter(nombre_completo__icontains=nombre_busqueda)
        resultados_patrocinadores = QuieroSerPatrocinador.objects.filter(nombre_completo__icontains=nombre_busqueda)
        
        if resultados_perros or resultados_gatos or resultados_patrocinadores:
            return render(request, 'resultados_busqueda.html', {'resultados_perros': resultados_perros,
                                                                'resultados_gatos': resultados_gatos,
                                                                'resultados_patrocinadores': resultados_patrocinadores})
        else:
            mensaje = f"No se encontró información para '{nombre_busqueda}'."
            return render(request, 'sin_resultados.html', {'mensaje': mensaje})

