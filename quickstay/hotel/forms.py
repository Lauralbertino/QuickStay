from django import forms
from .models import Hospede, Reserva

class HospedeForm(forms.ModelForm):
    class Meta:
        model = Hospede
        fields = ['nome', 'telefone', 'email']


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['hospede', 'quarto', 'check_in', 'check_out']
