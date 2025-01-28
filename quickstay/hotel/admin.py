# quickstay/hotel/admin.py
from django.contrib import admin
from .models import Hospede, Reserva, Quarto

# Registro do modelo Hospede
@admin.register(Hospede)
class HospedeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cidade', 'ocupacao')
    search_fields = ('nome', 'cpf', 'email')
    list_filter = ('cidade',)

# Registro do modelo Reserva
@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('hospede', 'quarto', 'check_in', 'check_out', 'status')
    search_fields = ('hospede__nome', 'quarto__numero')
    list_filter = ('status', 'check_in')

# Registro do modelo Quarto (caso necessário)
@admin.register(Quarto)
class QuartoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'tipo', 'preco_por_noite', 'capacidade')
    search_fields = ('numero', 'tipo')
    list_filter = ('tipo',)
