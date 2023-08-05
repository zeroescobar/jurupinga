import math
circleray = float(input("Qual o raio do circulo: "))
PI = math.pi
circlearea = PI * (circleray**2)
circleperi = 2 * PI * circleray
print(f"Raio: {circleray:.2f}\nArea: {circlearea:.2f}\nPerimetro: {circleperi:.2f}")