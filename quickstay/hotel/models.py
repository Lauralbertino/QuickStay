from django.db import models
from django.contrib.auth.models import User

class Hospede(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nome


class Quarto(models.Model):
    numero = models.IntegerField(unique=True)
    capacidade = models.IntegerField()
    preco_por_noite = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Quarto {self.numero}"


class Reserva(models.Model):
    hospede = models.ForeignKey(Hospede, on_delete=models.CASCADE)
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

    def calcular_valor_total(self):
        dias = (self.check_out - self.check_in).days
        return dias * self.quarto.preco_por_noite

    def __str__(self):
        return f"Reserva de {self.hospede.nome} no Quarto {self.quarto.numero}"
