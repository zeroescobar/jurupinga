
nome_arquivo = "numeros.txt"
arquivo = open(nome_arquivo,"w")

for n in range(1,101):
    arquivo.write(f"{n}\n")
arquivo.close()
