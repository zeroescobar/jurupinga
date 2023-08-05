def calcula_salario(salario, aumento_porcent):
    aumento = salario * (aumento_porcent / 100)
    novo_salario = salario+aumento
    return aumento,novo_salario
salario = float(input("Seu salario: "))
aumento_porcent = int(input("A porcentagem de aumento: "))
aumento,newSal = calcula_salario(salario=salario,aumento_porcent=aumento_porcent1200)
print(f"O valor do seu novo salario: {newSal} \n Aumento: {aumento}")