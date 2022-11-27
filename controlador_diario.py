from modelo_pagina import PaginaDiario
import json

class ControladorDiario:
    def __init__(self, usuario: str) -> None:
        self.usuario: str = usuario
        self.diario: dict = None # Json
    
    def conectar(self) -> None:
        '''Carrega ou relê o diário do usuário'''
        try:
            with open(f"diarios/{self.usuario}.json") as file:
                self.diario = json.load(file)
        except FileNotFoundError:
            with open(f"diarios/{self.usuario}.json", 'w') as file:
                # Cria um diário vazio
                json.dump([{"numero": n, "texto": [""]*10} for n in range(10)], file)
            self.conectar()

    def salvar_pagina(self, id: int, linhas: list[str]) -> None:
        '''Salva uma página no diário'''

        with open(f"diarios/{self.usuario}.json", 'r') as file:
            coisa = json.load(file)
         
        with open(f"diarios/{self.usuario}.json", 'w') as file:
            for pagina in coisa:
                if pagina['numero'] == id:
                    pagina['texto'] = linhas
                    json.dump(coisa, file)
        
        # Recarregar o diário após novo conteúdo ser salvo
        self.conectar()
                    

    def ler_pagina(self, n: int) -> PaginaDiario:
        return PaginaDiario(str(n), self.usuario, self.diario[n]["texto"])
    
    def criar_pagina(self):
        pass

    def remover_pagina(self):
        pass

    def alterar_pagina(self):
        pass