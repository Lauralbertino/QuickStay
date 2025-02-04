# quickstay/hotel/models.py
from django.db import models

class Instituicao(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    cidade= models.CharField(max_length=100)  

    def __str__(self):
        return self.nome
    
    # quickstay/hotel/models.py
class Hospede(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=15, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    ocupacao = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.nome

class Quarto(models.Model):
    numero = models.IntegerField()
    capacidade = models.IntegerField()
    preco_por_noite = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=100, default="Simples")  # Adicionando valor padrão

    def __str__(self):
        return f"Quarto {self.numero}"

class Reserva(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
    ]

    hospede = models.ForeignKey(Hospede, on_delete=models.CASCADE)
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')

    def __str__(self):
        return f"Reserva {self.id} - {self.hospede.nome} - Quarto {self.quarto.numero}"
