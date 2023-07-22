dias = int(input("Dias: "))
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))
minutosconv = minutos * 60
horasconv = horas * 60 * 60
diasconv = dias * 60 * 60 * 24
tempototal = minutosconv+segundos+horasconv+diasconv
print(f"Tempo total: {tempototal}")


