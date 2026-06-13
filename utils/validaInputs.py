from datetime import datetime


def ler_texto(mensagem):
    while True:
        valor = input(mensagem).strip()

        if valor: return valor

        print("Campo obrigatório.")

def ler_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem))

            if valor > 0: return valor

            print("O valor deve ser maior que zero.")

        except ValueError:
            print("Digite um número válido.")

def ler_int(mensagem):
    while True:
        try:
            valor = int(input(mensagem))

            if valor > 0: return valor

            print("O valor deve ser maior que zero.")

        except ValueError:
            print("Digite um número inteiro válido.")

def ler_data(mensagem):
    while True:
        data = input(mensagem)

        try:
            datetime.strptime(data, "%d/%m/%Y")
            return data

        except ValueError:
            print("Data inválida. Use DD/MM/AAAA.")
