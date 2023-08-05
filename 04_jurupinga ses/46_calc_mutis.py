velocidade = input("Qual velocidade?")
if velocidade.isnumeric:
    if velocidade > 80:
        excesso = velocidade - 80
        multa = excesso * 5
        print(f"Acima da velocidade, Valor da multa: R${multa:.2f}")
    else:
        print("Estás dentro da velocidade permitida")
else:
    print("Velocidade é um numero bobão")