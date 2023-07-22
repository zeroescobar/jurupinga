from_city = input("Cidade de origem: ")
to_city = input("Cidade de destino: ")
dist = int(input("Kms Percorridos: "))
gas_value = float(input("Valor da gasolina: "))
eta_value = float(input("Valor do etanol: "))
med_gas = float(input("Media de km p litro Gasolina: "))
med_eta = float(input("Media de km p litro etanol: "))
gast_km_gas = (1 / med_gas) * gas_value
gast_km_eta = (1 / med_eta) * eta_value
if gast_km_eta > gast_km_gas:
    print(f"Melhor usar gasolina pois gastará R${gast_km_gas:.2f} por km.")
elif gast_km_gas > gast_km_eta:
    print(f"Melhor usar etanol pois gastará R${gast_km_eta:.2f} por km.")
elif gast_km_gas == gast_km_eta:
    print(f"Ambos gastarão R${gast_km_eta:.2f} por km.")

print(f"Viagem de {from_city} para {to_city} de aproximadamente {dist} kms\n"
      f"Custo total da viagem sendo feita com gasolina:{gast_km_gas * dist} com a gasolina custando R${gas_value: .2f} e o carro fazendo uma media de {med_gas} kms p/ litro.\n"
      f"Custo total da viagem sendo feita com etanol:{gast_km_eta * dist} com a etanol custando R${eta_value: .2f} e o carro fazendo uma media de {med_eta} kms p/ litro.")