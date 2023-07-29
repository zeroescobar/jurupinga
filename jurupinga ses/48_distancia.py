dist = int(input("Distancia que voce deseja percorrer em Kms: "))
if dist>= 200:
    val_km = 0.45
else:
    val_km = 0.5
tot_val = dist*val_km
print(f"Preço a ser pago: R$ {tot_val:.2f}")