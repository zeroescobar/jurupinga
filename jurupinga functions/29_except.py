try:
    nota1 = int(input("nota 1: "))
    nota2 = int(input("nota 2: "))
    fator = int(input("fator: "))
    media = (nota1 + nota2) / fator
    print(f"MEdia: {media}")
except ValueError as erro:
    print("valor")
except ZeroDivisionError as erro:
    print("zero")
except Exception as erro:
    print("erro")