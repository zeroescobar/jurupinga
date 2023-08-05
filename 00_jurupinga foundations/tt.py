text = "How many persons? "
nb_person = int(input(text))
print(f"\33[1A\33[{len(text) + len(str(nb_person))}C persons")
