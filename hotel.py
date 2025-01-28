class Hospede:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def exibir_informacoes(self):
        print(f'Hóspede: {self.nome}, Telefone: {self.telefone}, Email: {self.email}')


class Quarto:
    def __init__(self, numero, capacidade, preco_por_noite):
        self.numero = numero
        self.capacidade = capacidade
        self.preco_por_noite = preco_por_noite

    def exibir_informacoes(self):
        print(f'Quarto {self.numero}: Capacidade: {self.capacidade}, Preço por Noite: R${self.preco_por_noite}')


class Reserva:
    def __init__(self, hospede, quarto, check_in, check_out):
        self.hospede = hospede
        self.quarto = quarto
        self.check_in = check_in
        self.check_out = check_out

    def calcular_valor_total(self):
        dias = (self.check_out - self.check_in).days
        valor_total = dias * self.quarto.preco_por_noite
        return valor_total

    def exibir_informacoes(self):
        print(f'Reserva para {self.hospede.nome}: Quarto {self.quarto.numero}, Check-in: {self.check_in}, Check-out: {self.check_out}, Valor Total: R${self.calcular_valor_total()}')


class Hotel:
    def __init__(self):
        self.quartos_disponiveis = []
        self.reservas = []

    def adicionar_quarto(self, quarto):
        self.quartos_disponiveis.append(quarto)

    def fazer_reserva(self, hospede, numero_quarto, check_in, check_out):
        for quarto in self.quartos_disponiveis:
            if quarto.numero == numero_quarto:
                reserva = Reserva(hospede, quarto, check_in, check_out)
                self.reservas.append(reserva)
                print(f'Reserva feita para {hospede.nome} no quarto {quarto.numero}.')
                return
        print(f'Quarto {numero_quarto} não disponível para as datas selecionadas.')


# Exemplo de uso
hospede1 = Hospede("João", "123456789", "joao@email.com")
quarto1 = Quarto(101, 2, 150)
hotel = Hotel()
hotel.adicionar_quarto(quarto1)

# Fazendo uma reserva
from datetime import datetime, timedelta

check_in = datetime(2023, 10, 1)
check_out = datetime(2023, 10, 5)
hotel.fazer_reserva(hospede1, 101, check_in, check_out)

# Exibindo informações da reserva
reserva = hotel.reservas[0]
reserva.exibir_informacoes()
