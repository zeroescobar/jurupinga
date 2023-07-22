salario = float(input("Seu salario: "))
aumento_porcent = int(input("A porcentagem de aumento: "))
aumento = salario * (aumento_porcent / 100)
novo_salario = salario+aumento
print("O valor do seu novo salario: ", novo_salario)