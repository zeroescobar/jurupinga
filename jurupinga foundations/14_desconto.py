while(True):
    nome = input("Nome do produto: ")
    preco = int(input(f"Preco de {nome}: "))
    desconto_percent = int(input(f"Desconto que sera dado para comprar {nome}: "))
    desconto = preco * (desconto_percent / 100)
    preco_final = preco - desconto
    tt = input(f"Desejas comprar {nome} por R${preco_final:.2f} ? \ndigite s para efetuar a compra: ")
    if tt == "s":
        print("Compra realizada com sucesso!!!!")
    else:
        print("A compra não foi realizada :(")
    tt2 = input("digite n para Sair ou qualquer outra tecla para reiniciar!")
    if tt2 == "n":
        break