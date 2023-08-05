numeros = [10,20,30,40,50,60,70,]


print(f"a lista tem {len(numeros)} elementos")

print(f"o item na posição 1 é o numero {numeros[1]}")

numeros[1] = 1000
print(f"{numeros[1]}")

numeros.append(124)
print(numeros)

print(numeros.pop(2))
print(numeros)
numeros.remove(10)
print(numeros)
del numeros[2]
print(numeros)
numeros.insert(0,100)
print(numeros)