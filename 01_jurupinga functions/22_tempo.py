def tempotoSecs(dias=0,horas=0,minutos=0,segundos=0):
    minutosconv = minutos * 60
    horasconv = horas * 60 * 60
    diasconv = dias * 60 * 60 * 24
    tempototal = minutosconv+segundos+horasconv+diasconv
    return tempototal
dias = int(input("Quantos dias: "))
horas = int(input("Quantas horas: "))
minutos = int(input("Quantos minutos: "))
segundos = int(input("Quantos segundos: "))
print(f"Há {tempotoSecs(dias=dias,horas=horas,minutos=minutos,segundos=segundos)} segundos em {dias} dias {horas} horas {minutos} minutos e {segundos} segundos")