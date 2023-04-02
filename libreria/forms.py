from django import forms
from .models import equipo

class equipoform(forms.ModelForm):
    class Meta:
        model = equipo
        fields = '__all__'