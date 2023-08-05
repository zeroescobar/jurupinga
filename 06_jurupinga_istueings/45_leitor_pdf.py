import tabula

dados = tabula.read_pdf("06_jurupinga_istueings/nota_alunos.pdf", 
                        encoding="latin-1",
                        pages="all")

tabula.convert_into("06_jurupinga_istueings/nota_alunos.pdf","06_jurupinga_istueings/nota_alunos.csv",
                    output_format = "csv",
                    pages="all")

print(dados)