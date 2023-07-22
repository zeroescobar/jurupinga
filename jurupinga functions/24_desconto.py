def calcula_desconto(preco,desconto_percent):
    desconto = preco * (desconto_percent /100)
    preco_final = preco - desconto
    return preco_final

def compra():
    nome = input("Nome do produto: ")
    preco = int(input(f"Preco de {nome}: "))
    desconto_percent = int(input(f"Desconto que sera dado para comprar {nome}: "))
    preco_final = calcula_desconto(preco=preco,desconto_percent=desconto_percent)
    tt = input(f"Desejas comprar {nome} por R${preco_final:.2f} ? \ndigite s para efetuar a compra: ")
    compra_realizada(tt)

def compra_realizada(repetir):
    return "Compra realizada com sucesso!!!!" if repetir == "s" else "A compra não foi realizada :("

while(True):
    compra()
    tt2 = input("digite n para Sair ou qualquer outra tecla para reiniciar!")
    if tt2 == "n":
        break