from escritor import EscritorCsv

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

nome_arquivo2 = "combusiveis.csv"
cabecalho2 = ["DIA","GASOLINA","ETANOL"]
dados2 = [
    ["segunda",5.66,3.20],
    ["terca",5.65,3.22],
    ["quarta",5.46,3.21],
    ["quinta",5.34,3.27],
    ["sexta",5.46,3.29],
    ["sabado",5.36,3.22],
    ["domingo",5.66,3.25]
]   
escritor = EscritorCsv(nome_arq=nome_arquivo,
                       cabecalho=cabecalho,
                       dados=dados)

escritor2 = EscritorCsv(nome_arq=nome_arquivo2,
                       cabecalho=cabecalho2,
                       dados=dados2)

escritor2.escrever()
escritor.escrever()