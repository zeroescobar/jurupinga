
class Combustiveis:
    def __init__(self, tipo, qtde_litros, valor_gasolina, valor_etanol):
        self.tipo           = tipo
        self.qtde_litros    = qtde_litros
        self.valor_gasolina = valor_gasolina
        self.valor_etanol   = valor_etanol


    def comprovante(self):
        print("\n")
        if self.tipo == "G":
            print(f"Foram colocados {self.qtde_litros} de {self.tipo}")
        elif self.tipo == "E":
            print(f"Foram colocados {self.qtde_litros} de {self.tipo}")
