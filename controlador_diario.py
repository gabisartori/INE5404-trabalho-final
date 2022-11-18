from pagina import PaginaDiario

class ControladorDiario:
    def __init__(self, usuario) -> None:
        self.usuario = usuario
        self.diario = []
    
    def conectar(self):
        try:
            file = open(f"diarios/{self.usuario}.txt", 'r')
            conteudo = file.readlines()
            paginas = []
            for linha in conteudo:
                a = linha.split(';')
                paginas.append([a[0], ''.join(a[1:])])
            self.diario = paginas
        except FileNotFoundError:
            return '????'

    def montar_pagina(self, id, linhas):
        string = str(id) + ';'
        for linha in linhas:
            string += linha + '&'
        return string[:-1]
    
    def salvar_pagina(self, id, linhas):
        pagina = self.montar_pagina(id, linhas)
        with open(f"diarios/{self.usuario}.txt", 'r') as file:
            conteudo = file.readlines()
            conteudo[id] = pagina
        
        with open(f"diarios/{self.usuario}.txt", 'w') as file:
            file.writelines(conteudo)
        

    def ler_pagina(self, n):
        return PaginaDiario(self.diario[n][0], self.usuario, self.diario[n][1])
    
    def criar_pagina(self):
        pass

    def remover_pagina(self):
        pass

    def alterar_pagina(self):
        pass