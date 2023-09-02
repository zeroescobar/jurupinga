import matplotlib.pyplot as plt
import pandas as pd

dados = pd.read_csv("chuvas_jan_2023.csv", delimiter=";")

plt.figure(figsize=(10,5))
plt.plot(dados['DIA'],dados['VALOR'])
plt.title("Informações de Chuva de Janeiro de 2023")
plt.xlabel("Dias")
plt.ylabel("Valores")

plt.xticks(dados["DIA"])
plt.savefig("chuvas_jan_2023.png")
plt.close("all")

