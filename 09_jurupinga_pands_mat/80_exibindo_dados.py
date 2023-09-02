import pandas as pd

tabela = pd.read_csv("temperaturas.csv")

print(f"informações com head \n{tabela.head()}")
print(f"Informações com tail \n{tabela.tail(50)}")
print(f"Informações com describe \n {tabela.describe()}")