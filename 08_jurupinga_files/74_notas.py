import csv
notas = []
def addnota(disciplina,aluno,nota1,nota2):
    dici = {
        "disciplina":disciplina,
        "aluno":aluno,
        "nota1":nota1,
        "nota2":nota2
    }
    notas.append(dici)
addnota("matematica","aluno01",5.89,7.1)
addnota("matematica","aluno02",6.9,9.9)
addnota("matematica","aluno03",3.6,8.78)
addnota("matematica","aluno04",2.78,7.4)
addnota("matematica","aluno01",6.12,3.12)
addnota("matematica","aluno02",9.43,4.67)
addnota("matematica","aluno03",7.31,4.9)
addnota("matematica","aluno04",4.12,1.23)
with open("74_notas.csv", "w", encoding="UTF-8", newline="") as f:
    escritor = csv.writer(f)
    escritor.writerow(['DISCIPLINA','ALUNO','N1','N2'])

    for nota in notas:
        disciplina = nota.get("disciplina")
        aluno = nota.get("aluno")
        n1 = nota.get("nota1")
        n2 = nota.get("nota2")
        escritor.writerow([disciplina,aluno,n1,n2])


