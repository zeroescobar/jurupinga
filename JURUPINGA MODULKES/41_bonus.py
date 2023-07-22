recarga = int(input("Recarga: "))
bonus = 0

if recarga == 15:
    bonus = 200
elif recarga == 25:
    bonus = 300
elif recarga == 40:
    bonus = 450

print(f"Carregou R${recarga},00 e ganhou {bonus} Mbs de bonus de internet")