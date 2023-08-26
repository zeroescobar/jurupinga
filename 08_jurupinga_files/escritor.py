import csv
class EscritorCsv:
    def __init__(self, nome_arq,cabecalho,dados):
        self.nome_arq = nome_arq
        self.cabecalho = cabecalho
        self.dados = dados
    
    def escrever(self):
        #verificar o tipo da primeira linha
        p_linha = self.dados[0]
        if isinstance(p_linha,dict) or isinstance(p_linha,list):
            self.savecsv(
                nome_arq=self.nome_arq,
                cabecalho=self.cabecalho,
                dados=self.convert_dict_to_list(self.dados) if isinstance(p_linha,dict) else self.dados
                )
        else:
            print("tome no seu cu")
    def convert_dict_to_list(self,dict):
        lista = []
        for dado in dict:
            lista.append(dado.values())
        return lista
    
    def savecsv(self, nome_arq,cabecalho, dados):
        with open(nome_arq, "w", encoding="UTF-8", newline="") as arq:
                wrt = csv.writer(arq)
                wrt.writerow(cabecalho)
                wrt.writerows(dados)
