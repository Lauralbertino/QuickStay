from django.shortcuts import render, redirect
from .models import Hospede, Quarto, Reserva,Instituicao 
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

def editar_hospede(request, id):
    hospede = get_object_or_404(Hospede, id=id)
    
    if request.method == 'POST':
        form = HospedeForm(request.POST, instance=hospede)
        if form.is_valid():
            form.save()
            return redirect('listar_hospedes')  # Redireciona para a lista de hóspedes
    else:
        form = HospedeForm(instance=hospede)

    return render(request, 'editar_hospede.html', {'form': form, 'hospede': hospede})

def deletar_hospede(request, id):
    hospede = get_object_or_404(Hospede, id=id)
    if request.method == 'POST':
        hospede.delete()
        return redirect('listar_hospedes')  # Redireciona para a lista de hóspedes
    
    return render(request, 'confirmar_delecao.html', {'hospede': hospede})

def listar_quartos(request):
    quartos = Quarto.objects.all()
    return render(request, "listar_quartos.html", {"quartos":quartos })

def listar_instituicoes(request):
    instituicoes = Instituicao.objects.all()
    return render(request, "listar_instituicoes.html", {"instituicoes": instituicoes})
