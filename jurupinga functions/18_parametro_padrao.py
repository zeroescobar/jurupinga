def calc_gasto_fuel(km, value, media_km=9):
    qtde_litros = km/ media_km
    valor_total = qtde_litros * value
    return valor_total
km=300
valor_fuel = 5.45
km_litro = 12

rs01 = calc_gasto_fuel(km, valor_fuel, km_litro)

rs02 = calc_gasto_fuel(km, valor_fuel)
print(f"valor 1: {rs01:.2f}")
print(f"valor 2: {rs02:.2f}")