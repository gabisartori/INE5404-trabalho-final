from pagina import Pagina


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
                a = linha.split()
                paginas.append([a[0], ''.join(a[1:])])
            self.diario = paginas
        except FileNotFoundError:
            return '????'

    def ler_pagina(self, n):
        return Pagina(self.diario[n][0], self.usuario, self.diario[n][1])
    
    def criar_pagina(self):
        pass

    def remover_pagina(self):
        pass

    def alterar_pagina(self):
        pass