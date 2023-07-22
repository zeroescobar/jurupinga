"""
200 - 0,01
500 - 0,10
750 - 0,25
750< - 0,35
"""
valor = float(input("Valor  da compra: "))
desconto = 0
if valor == 200:
    desconto = 0.01
elif valor == 500:
    desconto = 0.10
elif valor == 750:
    desconto = 0.25
elif valor > 750:
    desconto = 0.35
else:
    desconto = 0.00
valordesconto = valor * desconto
valorfinal = valor - valordesconto
print(f"Nota fiscal:\n Valor da compra: R${valor:.2f}\n Valor desconto: R${valordesconto:.2f}\n Valor total:  R${valorfinal:.2f}")
