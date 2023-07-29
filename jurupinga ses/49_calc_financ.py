valor = float(input("Valor da casa: "))
salario = float(input("Seu salario: "))
anos = int(input("Quer financiar para pagar em quantos anos: "))
meses = anos * 12
valor_prest = valor / meses
percent_sal = salario * 0.3
if valor_prest < percent_sal:
    print(f"achas que consegue esmagar a minha rata?\n valor das parcelas: R${valor_prest:.2f}\n quantidade de parcelas: {meses}")
else:
    print("NEGADOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")

