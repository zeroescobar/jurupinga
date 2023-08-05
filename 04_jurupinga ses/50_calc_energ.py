quantkwh = float(input("Quantidade de Kw/h: "))
print("digite R para Residencial, I para Industrial, e C para Comercial")
tipoinst = input("Qual o tipo da sua instalação eletrica? ")
preco = 0
if tipoinst == "R" or tipoinst == "r":
    if quantkwh > 500:
        preco = 0.65
    else:
        preco = 0.4
elif tipoinst == "I" or tipoinst == "i":
    if quantkwh > 5000:
        preco = 0.60
    else:
        preco = 0.55
elif tipoinst == "C" or tipoinst == "c":
    if quantkwh > 1000:
        preco = 0.60
    else:
        preco = 0.55
else:
    print("Instalacao não identificada")
tot_prec = quantkwh * preco if preco > 0 else 0
print(f"Preço a ser pago: R$ {tot_prec:.2f}\nPreço Kw/h: R$ {preco:.2f}")