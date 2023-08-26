import csv
nome_arquivo = "combusiveis.csv"
cabecalho = ["DIA","GASOLINA","ETANOL"]
dados = [
    ["segunda",5.66,3.20],
    ["terca",5.65,3.22],
    ["quarta",5.46,3.21],
    ["quinta",5.34,3.27],
    ["sexta",5.46,3.29],
    ["sabado",5.36,3.22],
    ["domingo",5.66,3.25]
]

with open(nome_arquivo, "w", encoding="UTF-8", newline="") as file:
    wrt = csv.writer(file)
    wrt.writerow(cabecalho)
    wrt.writerows(dados)