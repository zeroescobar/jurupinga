num =1
pares = []

while num<=100:
    if num % 2 == 0:
        print(num)
        pares.append(num)
    num+=1
    if len(pares) >= 10:
        break

print(len(pares))