payment = int(input("Ganhas quanto: "))
percentage_increase = int(input("Sua promoção"))

value_increase = payment * (percentage_increase / 100)
new_payment = payment + value_increase
print(new_payment)