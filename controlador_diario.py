from pagina import PaginaDiario
import json

class ControladorDiario:
    def __init__(self, usuario) -> None:
        self.usuario = usuario
        self.diario = None
    
    def conectar(self):
        try:
            with open(f"diarios/{self.usuario}.json") as file:
                self.diario = json.load(file)
        except FileNotFoundError:
            with open(f"diarios/{self.usuario}.json", 'w') as file:
                json.dump([], file)
            self.conectar()

    def montar_pagina(self, id, linhas):
        
        
        string = str(id) + ';'
        for linha in linhas:
            print(linha)
            string += linha + '&'
        return string[:-1] + '\n'
    
    def salvar_pagina(self, id, linhas):
        self.conectar()
        with open(f"diarios/{self.usuario}.json", 'r') as file:
            coisa = json.load(file)
         
        with open(f"diarios/{self.usuario}.json", 'w') as file:
            for pagina in coisa:
                if pagina['numero'] == id:
                    pagina['linhas'] = linhas
                    json.dump(coisa, file)
                    return
                    

    def ler_pagina(self, n):
        return PaginaDiario(str(n), self.usuario, self.diario[n]["texto"])
    
    def criar_pagina(self):
        pass

    def remover_pagina(self):
        pass

    def alterar_pagina(self):
        pass