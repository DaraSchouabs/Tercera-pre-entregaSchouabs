from django import forms
from BacoPet.models import AdopcionPerro, AdopcionGato, QuieroSerPatrocinador, Persona

class AdopcionPerroForm(forms.ModelForm):
    class Meta:
        model = AdopcionPerro
        fields = '__all__'

class AdopcionGatoForm(forms.ModelForm):
    class Meta:
        model = AdopcionGato
        fields = '__all__'

class QuieroSerPatrocinadorForm(forms.ModelForm):
    class Meta:
        model = QuieroSerPatrocinador
        fields = '__all__'
        
class BusquedaForm(forms.Form):
    nombre = forms.CharField(label='Buscar Persona')

    def __init__(self, *args, **kwargs):
        super(BusquedaForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['placeholder'] = 'Buscar persona'
