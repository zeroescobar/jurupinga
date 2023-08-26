import requests
import json
import csv
from time import sleep


url = "https://loteriascaixa-api.herokuapp.com/api/megasena"

concursos = [2624,2623,2622,2621]
cons_data = []
resultado = requests.get(url).json()
for concurso in resultado:
    data = {
        "data": concurso.get("data"),
        "dezenas": concurso.get("dezenas")
    }
    cons_data.append(data)
    sleep(0.01)
'''
for concurso in concursos:
    url_completa = f"{url}/{concurso}"
    result = requests.get(url_completa).json()
    data = {
        "data": result.get("data"),
        "dezenas": result.get("dezenas")
    }
    cons_data.append(data)
    sleep(0.1)
'''

print(cons_data)

cabecalho = ["DATA","D1","D2","D3","D4", "D5", "D6"]

with open("mesena.csv", "w", encoding="UTF-8", newline="") as arq:
          escritor = csv.writer(arq)
          escritor.writerow(cabecalho)
          for item in cons_data:
            lista = []
            lista.append(item.get("data"))
            for it in item.get("dezenas"):
                 lista.append(int(it))
            escritor.writerow(lista) 