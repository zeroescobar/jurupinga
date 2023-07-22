import calculo_media

med = []
while True:
    tt = input("Digite um numero ou n para sair: ")
    if tt.isnumeric():
        med.append(int(tt))
    elif tt == "n":
        break
print(f"Media: {calculo_media.media(list=med)}")