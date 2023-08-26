with open("alunos.txt", "r", encoding="UTF-8") as file:
    for aluno in file.readlines():
        print(f"Aluno {aluno}")