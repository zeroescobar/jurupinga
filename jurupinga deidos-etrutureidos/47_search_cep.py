import requests
import json

cep = int(input("DIgite o seu cep: (Somente numeros) "))
url = f"https://viacep.com.br/ws/{cep}/json"

response = requests.get(url)
if response.status_code == 200:
    print(json.dumps(response.json(),indent=4))
    print(response.json().get("logradouro"))
