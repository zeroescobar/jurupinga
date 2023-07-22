def calcular_qtde_litros(dist,km_litro):
    qtde_litros = dist / km_litro
    return qtde_litros

def calcular_valor_gasto(qtde,valor=5.45):
    gasto = qtde * valor
    return gasto

cid_saida = input("Informe sua cidade de origem: ")
cid_destino = input("Informe sua cidade de destino: ")
dist = int(input("Informe em Kms a distancia que será percorrida: "))
km_litro = float(input("Informe quantos KM por litro seu carro faz: "))
combust = input("Informe o combustivel que sera usado por seu carro: ")
valor = float(input("Informe o valor do combustivel que sera usado: "))

qtde_litros = calcular_qtde_litros(dist=dist,km_litro=km_litro)
gasto = calcular_valor_gasto(qtde=qtde_litros,valor=valor)

print(f"Quantidade aproximada de litros gastos: {qtde_litros}\n Gasto total com combustivel: {gasto}")
