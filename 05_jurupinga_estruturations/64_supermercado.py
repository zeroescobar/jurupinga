itens = [
{"produto": "café", "valor": 16.99, "qtde": 1, "categoria": "alimentação"},
{"produto": "leite", "valor": 3.99, "qtde": 1, "categoria": "alimentação"},
{"produto": "pão", "valor": 0.99, "qtde": 8, "categoria": "alimentação"},
{"produto": "detergente", "valor": 1.99, "qtde": 5, "categoria": "limpeza"},
{"produto": "bombril", "valor": 2.99, "qtde": 2, "categoria": "limpeza"},
{"produto": "desinfetante", "valor": 6.99, "qtde": 3, "categoria": "limpeza"},
{"produto": "papel higienico", "valor": 36.99, "qtde": 2, "categoria": "limpeza"},
{"produto": "sabão em pó", "valor": 21.99, "qtde": 2, "categoria": "limpeza"},
{"produto": "carne seca", "valor": 26.99, "qtde": 1, "categoria": "açougue"},
{"produto": "coxa frango", "valor": 23.99, "qtde": 2, "categoria": "açougue"},
]

values_total = {
    'alimentação':0,
    'limpeza':0,
    'açougue':0,
    'tudo':0
}
for prod in itens:
    total_produto = prod.get("qtde") * prod.get("valor")
    values_total[prod.get("categoria")] += total_produto
    values_total['tudo'] += total_produto

[print(f"Total de {categ} : R$ {total:.2f}") for categ, total in values_total.items()]