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
                json.dump([{"numero": n, "texto": [""]*10} for n in range(10)], file)
            self.conectar()

    def salvar_pagina(self, id, linhas):
        with open(f"diarios/{self.usuario}.json", 'r') as file:
            coisa = json.load(file)
         
        with open(f"diarios/{self.usuario}.json", 'w') as file:
            for pagina in coisa:
                if pagina['numero'] == id:
                    pagina['texto'] = linhas
                    json.dump(coisa, file)
        self.conectar()
                    

    def ler_pagina(self, n):
        return PaginaDiario(str(n), self.usuario, self.diario[n]["texto"])
    
    def criar_pagina(self):
        pass

    def remover_pagina(self):
        pass

    def alterar_pagina(self):
        pass