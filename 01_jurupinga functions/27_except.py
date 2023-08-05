def calculo(n1,n2):
    return n1/n2

try:
    calculo(1,ndf)
except Exception as error:
    print(f"ERRO: {error}")
finally:
    print("terminou")