try:
    numeros = [1,52,5235,23]
    print(numeros[5])
except IndexError as erro:
    print(erro)
finally:
    print("terminei :)")