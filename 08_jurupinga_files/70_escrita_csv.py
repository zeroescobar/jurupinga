import csv
nome_arquivo = "temperaturas.csv"
cabecalho = ["DIA DA SEMANA","TEMPERATURA"]
dados = [
    {"dia":"segunda-feira","temperatura":29.6},
    {"dia":"terça-feira","temperatura":27.2},
    {"dia":"quarta-feira","temperatura":23.2},
    {"dia":"quinta feira","temperatura":11},
    {"dia":"sexta-feira","temperatura":12},
    {"dia":"sabado-feria","temperatura":13},
    {"dia":"domingo-feria","temperatura":222}
]

with open(nome_arquivo, "w", encoding="UTF-8", newline="") as file:
    escritor = csv.writer(file)
    escritor.writerow(cabecalho)

    for info in dados:
        dia_semana = info.get("dia")
        temperatura = info.get("temperatura")
        escritor.writerow([dia_semana,temperatura])
