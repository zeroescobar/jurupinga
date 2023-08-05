animais = [
    {
        "nome":"Cachorro Pastor",
        "idade":3,
        "fator_idade":12
    },
    {
        "nome":"Cachorro Fila",
        "idade":4,
        "fator_idade":10
    },
    {
        "nome":"Cachorro Golden",
        "idade":2,
        "fator_idade":8
    },
    {
        "nome":"Papagaio",
        "idade":8,
        "fator_idade":5
    },
    {
        "nome":"Gato_siame",
        "idade":4,
        "fator_idade":7
    },
    {
        "nome":"Cachorro Husky",
        "idade":3,
        "fator_idade":9
    }
]

for animal in animais:
    idade = animal.get("idade") * animal.get("fator_idade")
    if idade > 30 and animal.get("nome").__contains__("Cachorro"):
        print(f'Animal: {animal.get("nome")}\nIdade humana: {idade}')