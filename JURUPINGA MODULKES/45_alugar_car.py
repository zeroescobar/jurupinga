"""----------Promoção por diária------------
PERIODO                 VALOR_DIARIA
De 2 até 5 dias       R$ 105,00
De 6 até 15 dias     R$ 95,00
De 16 até 25 dias    R$ 70,00
Acima de 25 dias     R$ 60,00

-------Promoção por kilometragem---------
KM RODADO            VALOR POR KM
De 100 até 1000      R$ 6,99
De 1001 até 4000     R$ 4,99
De 4001 até 6000     R$ 3,99
Acima de 6000        R$ 2,99

A empresa vai oferecer simulação dos dois planos e com base na inteligência artificial do nosso algoritmo será mostrado para o usuário
a seguinte mensagem ao final:

Com base na simulação realizada segue as informações:
------Plano por diária------
Total dias ?, valor gasto ?

------Plano por kilometragem------
Total kilometros ?, valor gasto ?"""

def valor_diaria(periodo):
    valor = 0
    if periodo>=2 and periodo <= 5:
        valor = 105
    elif periodo >=6 and periodo <= 15:
        valor = 95
    elif periodo >= 16 and periodo <=25:
        valor = 70
    elif periodo >= 25:
        valor = 60
    return valor

def valor_km(dist):
    valor = 0.00
    if dist>=100 and dist <= 1000:
        valor = 6.99
    elif dist >=1001 and dist <= 4000:
        valor = 4.99
    elif dist >= 4001 and dist <=6000:
        valor = 3.99
    elif dist >= 6001:
        valor = 2.99
    return valor

dias = int(input("Quantidade de dias que pretende usar o carro: "))
kms = int(input("Quantidade de kms que deseja rodar: "))
val_dia = valor_diaria(dias)
val_km = valor_km(kms)
price_dia = val_dia * dias
price_kms = val_km * kms
print(f"Com base na simulação realizada segue as informações:\n"
      f"------Plano por diária------\n"
      f"Total dias {dias}, valor gasto {price_dia}\n"
      f"\n"
      f"------Plano por kilometragem------\n"
      f"Total kilometros {kms}, valor gasto {price_kms}\n"
      f"\n")
if price_kms > price_dia:
    print("Recomendamos usar o plano por Diaria :)")
elif price_dia > price_kms:
    print("Recomendamos usar o plano por Kilometragem :)")
elif price_dia == price_kms:
    print("Ambos os planos terão o mesmo custo na sua situação, fique a vontade!!")