from pandas import DataFrame,Series

notas_alunos = {
    "alunos":Series(data=["aluno01","aluno02","aluno03"]),
    "notas_p1": Series(data=[2.9,1.2,9.0]),
    "notas_p2": Series(data=[4.9,2.2,7.1])
}

tabela = DataFrame(notas_alunos)
print(f"Exibindo tabela\n{tabela}")
print(tabela.info())
print(tabela.size)
print(tabela.memory_usage())

tabela_filtrada = DataFrame(notas_alunos, index=[0,2])
print(f"Exibindo dados filtrados \n {tabela_filtrada}")

tabela_colunas = DataFrame(notas_alunos,columns=["alunos","notas_p2"])
print(f"Exibindo dados de colunas \n {tabela_colunas}")

