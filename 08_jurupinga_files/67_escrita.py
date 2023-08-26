alunos = ["João","Maria","Silvia"]
with open("alunos.txt","w", encoding="UTF8") as arq:
    for aluno in alunos:
        arq.write(f"{aluno}\n")