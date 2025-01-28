from django.shortcuts import render, redirect
from .models import Hospede, Quarto, Reserva
from .forms import HospedeForm, ReservaForm

def home(request):
    return render(request, "home.html")

def listar_hospedes(request):
    hospedes = Hospede.objects.all()
    return render(request, "listar_hospedes.html", {"hospedes": hospedes})

def criar_hospede(request):
    if request.method == "POST":
        form = HospedeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_hospedes")
    else:
        form = HospedeForm()
    return render(request, "criar_hospede.html", {"form": form})

def listar_reservas(request):
    reservas = Reserva.objects.select_related('hospede', 'quarto').all()
    return render(request, "listar_reservas.html", {"reservas": reservas})

def criar_reserva(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_reservas")
    else:
        form = ReservaForm()
    return render(request, "criar_reserva.html", {"form": form})
