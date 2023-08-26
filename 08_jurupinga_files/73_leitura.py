import csv
nome_arquivo = "combusiveis.csv"
with open(nome_arquivo, "r", encoding="UTF-8", newline="") as arq:
    leitor = csv.reader(arq)
    for indice, linha in enumerate(leitor):
        if indice > 0:
                dia = linha[0]
                valor_g = linha[1]
                valor_e = linha[2]
                print(f"Dia {dia}, \nGasolina {valor_g}, \nEtanol {valor_e}")