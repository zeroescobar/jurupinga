
class PagSeguro:
    def __init__(self, valor, operacao):
        self.valor    = valor
        self.operacao = operacao

    def calcular_valor_parcela(self, qtde_parcelas):
        valor_parcela = self.valor / qtde_parcelas
        return valor_parcela

    def comprovante(self, qtde_parcelas, valor_parcela):
        print("\n")
        if self.operacao == "D":
            print(f"comprovante de venda \n")
            print(f"operaçao debito\n")
            print(f"R$ {self.valor}")
        elif self.operacao == "C":
            print(f"comprovante de venda \n")
            print(f"operaçao credito\n")
            print(f"R$ {self.valor}")
            print(f"{qtde_parcelas} x sem juros de R${valor_parcela}")




