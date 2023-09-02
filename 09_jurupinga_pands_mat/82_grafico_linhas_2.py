import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

nome = "INMET_CO_DF_A001_BRASILIA_01-01-2022_A_31-12-2022.CSV"
dados = pd.read_csv(nome,
                    delimiter=";",
                    on_bad_lines="skip",
                    encoding="latin-1",
                    skiprows=8)
print(dados.head())
print(dados.columns)
print(dados["Data"])
print(dados["PRECIPITAÇÃO TOTAL, HORÁRIO (mm)"])

meses = [
    {"mes_numero":1, "mes_nome":"Jan", "total_chuva":0.0},
    {"mes_numero":2, "mes_nome":"Fev", "total_chuva":0.0},
    {"mes_numero":3, "mes_nome":"Mar", "total_chuva":0.0},
    {"mes_numero":4, "mes_nome":"Abr", "total_chuva":0.0},
    {"mes_numero":5, "mes_nome":"Mai", "total_chuva":0.0},
    {"mes_numero":6, "mes_nome":"Jun", "total_chuva":0.0},
    {"mes_numero":7, "mes_nome":"Jul", "total_chuva":0.0},
    {"mes_numero":8, "mes_nome":"Ago", "total_chuva":0.0},
    {"mes_numero":9, "mes_nome":"Set", "total_chuva":0.0},
    {"mes_numero":10, "mes_nome":"Out", "total_chuva":0.0},
    {"mes_numero":11, "mes_nome":"Nov", "total_chuva":0.0},
    {"mes_numero":12, "mes_nome":"Dez", "total_chuva":0.0},
]

for indice, linha in dados.iterrows():
    data = datetime.strptime(linha["Data"], '%Y/%m/%d').date()
    mes = data.month
    # tratando a chuva
    chuva = str(linha["PRECIPITAÇÃO TOTAL, HORÁRIO (mm)"])
    chuva = float(chuva.replace(",","."))
    if indice == 0:
        print(data)

    for mes_dict in meses:
        if mes_dict["mes_numero"] == mes:
            mes_dict["total_chuva"] += chuva

dados_grafico =[
    [],[]
]
for mes_d in meses:
    if mes_d["total_chuva"] > 0:
        dados_grafico[0].append(mes_d["mes_nome"])
        dados_grafico[1].append(mes_d["total_chuva"])

plt.figure(figsize=(10,5))
plt.pie(dados_grafico[1], labels=dados_grafico[0])
plt.title("Informações chuva 2022")
plt.xlabel("Meses")
plt.ylabel("Valores")
plt.xticks(dados_grafico[0])
plt.savefig("chuvas2022.png")
plt.close("all")
