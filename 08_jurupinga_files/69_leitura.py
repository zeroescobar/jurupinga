try:
    with open("alunos.txt","r",encoding="UTF-8", newline="") as file:
        for aluno in file.readlines():
            a= aluno.replace("\n", "")
            print(f"Aluno {a}")
except FileNotFoundError:
    print("Arquivo não encontrado")