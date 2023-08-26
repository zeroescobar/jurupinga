from classes_combustiveis import Combustiveis

def operacao():
    qtde_litros = int(input("Digite a qtde de litros:"))
    tipo        = input("Você deseja Gasolina [G] ou Etanol [E]?")
    valor_gaso  = 10
    valor_eta   = 3.56

    combustivel = Combustiveis(tipo, qtde_litros, valor_gaso, valor_eta)

    def calcular_comb(qtde_litros, valor):
        valor_total = qtde_litros * valor
        return valor_total

    valor_total_gaso = calcular_comb(qtde_litros, valor_gaso)
    valor_total_eta  = calcular_comb(qtde_litros, valor_eta)


    if tipo == "G" or valor_total_gaso < 150:
        combustivel.comprovante()
        print(valor_total_gaso)
    elif tipo == "E" or valor_total_eta < 150:
        combustivel.comprovante()
        print(valor_total_eta)
    parcela = ""
    if valor_total_gaso > 150 or valor_total_eta > 150:
        parcela = input("Você deseja parcelar? [S] ou [N]:")
    if  parcela == "S" and valor_total_gaso > 150:
        num_parcelas = int(input("Digite o número de parcelas:"))
        combustivel.comprovante()
        print(num_parcelas)
        valor_parcelador = valor_total_gaso / num_parcelas
        print(valor_parcelador)
    if parcela == "S" and valor_total_eta > 150:
        num_parcelas = int(input("Digite o número de parcelas:"))
        combustivel.comprovante()
        print(num_parcelas)
        valor_parcelador = valor_total_eta / num_parcelas
        print(valor_parcelador)

    elif parcela == "N" and valor_total_gaso > 150:
        combustivel.comprovante()
        print(valor_total_gaso)
    elif parcela == "N" and valor_total_eta > 150:
        combustivel.comprovante()
        print(valor_total_gaso)


operacao()