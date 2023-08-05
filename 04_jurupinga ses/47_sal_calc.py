salario = int(input("Digite seu salario: "))
if salario >= 1350:
    aumento = 0.10
else:
    aumento = 0.15
val_aumento =salario* aumento
salario += val_aumento
print(f"--------------------\nSalario novo: R$ {salario:.2f}\n--------------------\nValor do aumento: R$ {val_aumento:.2f}\n-------------------- ")
    