from datetime import datetime
import json

aluno = dict(nome="Sergio",idade=22,cidade="Santos")
print(f"O aluno tem as propriedades {aluno}")

aluno2 = {
    "nome":"Sergio",
    "idade" : 22,
    "cidade" : "Santos"
}
print(f"O aluno tem as propriedades {aluno}")

aluno_elet = {
    "nome":"Elias",
    "idade":19,
    "cidade":"Piracicaba",
    "aluno_senai": True,
    "disciplinas":["Comandos Eletricos","CLP"],
    "matriculado": False,
    "date": str(datetime.now()),
    "endereco": {
        "logradouro":"Rua 10, 560",
        "bairro":"Jardim das Flores",
        "cidade":"Santos",
        "cep": 13421832,
        "uf": "sp"
    }
}
print(aluno_elet)
print(f'aluno: {aluno_elet.get("nome")}')
print(f'endreco: {aluno_elet.get("endereco")}')
#print(f'idade: {aluno_elet["idadeas"]}')
print(json.dumps(aluno_elet,
                 indent=4))

disci = aluno_elet.get("disciplinas")
print(disci[1])
bairro = aluno_elet.get("endereco").get("bairro")
print(bairro)

aluno_elet.get("disciplinas").append("Eletronica Analogica")
print(aluno_elet)

aluno_elet["endereco"]["cep"] = 123
print(aluno_elet)