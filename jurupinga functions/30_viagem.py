def calcula_viagem(km,valor_comb,media_veiculo):
    qtde_litros = km / media_veiculo
    total = qtde_litros * valor_comb
    print(f"Vai gastar: {total:.2f}")

try:
    kilometros = int(input("km: "))
    valor = float(input("Valor: "))
    media = int(input("Media: "))
    calcula_viagem(kilometros,valor,media)
except Exception as ex:
    print(f"ERRO: {ex}")