from modelo_pagina import PaginaDiario
import json


class ControladorDiario:
    def __init__(self, usuario: str) -> None:
        self.__usuario: str = usuario
        self.__diario: dict | None = None  # Json

    def conectar(self) -> None:
        """Carrega ou relê o diário do usuário"""
        try:
            with open(f"diarios/{self.__usuario}.json") as file:
                self.__diario = json.load(file)
        except FileNotFoundError:
            with open(f"diarios/{self.__usuario}.json", 'w') as file:
                # Cria um diário vazio
                json.dump([{"numero": n, "texto": [""]*10} for n in range(10)], file)
            self.conectar()

    def salvar_pagina(self, id: int, linhas: list[str]) -> None:
        """Salva uma página no diário"""

        with open(f"diarios/{self.__usuario}.json", 'r') as file:
            coisa = json.load(file)

        with open(f"diarios/{self.__usuario}.json", 'w') as file:
            for pagina in coisa:
                if pagina['numero'] == id:
                    pagina['texto'] = linhas
                    json.dump(coisa, file)

        # Recarregar o diário após novo conteúdo ser salvo
        self.conectar()

    def ler_pagina(self, n: int) -> PaginaDiario:
        return PaginaDiario(n, self.__usuario, self.__diario[n]["texto"])
    
    def get_diario(self) -> dict:
        return self.__diario
    
    def get_usuario(self) -> str:
        return self.__usuario
    
