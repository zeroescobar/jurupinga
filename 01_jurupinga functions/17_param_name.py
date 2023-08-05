def calcula_aumento_salario(sal, percent):
    valor_aumento = sal * (percent / 100)
    novo_salario = sal + valor_aumento
    return novo_salario

sal_at = 8000
percent = 10
sal_novo = calcula_aumento_salario(sal=sal_at,percent=percent)
print(f"O novo salario é: {sal_novo}")