cid_saida = input("Informe sua cidade de origem: ")
cid_destino = input("Informe sua cidade de destino: ")
dist = int(input("Informe em Kms a distancia que será percorrida: "))
km_litro = float(input("Informe quantos KM por litro seu carro faz: "))
combust = input("Informe o combustivel que sera usado por seu carro: ")
valor = float(input("Informe o valor do combustivel que sera usado: "))
qtde_litros = dist / km_litro
gasto = qtde_litros*valor
print(f"Quantidade aproximada de litros gastos: {qtde_litros}\n Gasto total com combustivel: {gasto}")
