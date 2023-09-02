import pandas as pd
from random import randint
import json
import os
import psutil
temperaturas = {}
total = 60 * 24 
dias = 30 
writer = pd.ExcelWriter("temp.xlsx", engine="openpyxl")
for dia in range(1,dias):
    chave = "dia_"+ str(dia)
    temperaturas[chave] = []
    for periodo in range(1,total):
        valor_temp = randint(5,38)
        temperaturas[chave].append(valor_temp)
    print(f"criou {chave}")
    """sheet = pd.DataFrame(temperaturas[chave])
    sheet.to_excel(writer,sheet_name=chave, index=False)
    writer._save()"""

with pd.ExcelWriter("temp3.xlsx",engine="xlsxwriter") as writer:
    for chave, dados in temperaturas.items():
        df = pd.DataFrame({chave:dados})
        df.to_excel(writer,sheet_name=chave, index=False)


def verificar_arquivo_aberto(caminho):
    esta_aberto = False
    for prc in psutil.process_iter(
        attrs=["pid","name"]):
        arquivos_abertos = prc.open_files()
        for arquivo_aberto in arquivos_abertos:
            if arquivo_aberto.path == caminho:
                esta_aberto = True
                break
    return esta_aberto

tabela = pd.DataFrame(temperaturas)
nome_arq = "temperaturas.csv"
if os.path.isfile(nome_arq):
    arquivo_em_edicao = verificar_arquivo_aberto(nome_arq)
    if arquivo_em_edicao:
        print("Arquivo aberto")
else:
    tabela.to_csv(nome_arq)