from PagSeguro import PagSeguro

def calcular():
    print("Seja bem vindo ao PagSeguro, Vamos calcular sua venda:")
    valor    = float(input("Valor total do produto:"))
    operacao = (input("Operacao: [D] para Débito e [C] para Crédito:"))

    pagseguro = PagSeguro(valor,operacao)

    if operacao == "D":
        pagseguro.comprovante(1, valor)
    elif operacao == "C":
        qtde_parcelas = int(input("Qtde de Parcelas:"))
        valor_parcela = pagseguro.calcular_valor_parcela(qtde_parcelas)
        pagseguro.comprovante(qtde_parcelas, valor_parcela)

    print("\n")
    continuar = input("Deseja realizar outra venda? [S] ou [N]:")

    if continuar == "S":
        calcular()


calcular()