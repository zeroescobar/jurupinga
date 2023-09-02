import pandas as pd

notas = [3.9,20,1.3,7.8,9.0]

serie = pd.Series(data=notas)
print(f"A informação da serie é \n{serie}")
estatistica = serie.describe()
print(estatistica)
print(f"{estatistica.get('25%')}")

serie_index = pd.Series(data=notas,
                        index=[10,11,12,13,14])
print(f"2-A a iformação da serie é \n{serie_index}")

d_notas = {
    "aluno01":4.9,
    "aluno02":7.2,
    "aluno03":1.1,
    "aluno04":9.9
}

serie_dicionario = pd.Series(data=d_notas)
print(f"3-A a informação das notas é \n{serie_dicionario}")