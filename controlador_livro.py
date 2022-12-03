from modelo_pagina import Pagina
import os


class ControladorLivro:
    def __init__(self) -> None:
        self.__livro: list[Pagina] = []
    
    def conectar_livro(self, livro: str) -> None:
        """Carrega o conteúdo do livro"""
        try:
            arquivo = open("livros/" + livro + ".txt", "r")
            conteudo = arquivo.readlines()
            paginas = []
            for linha in conteudo:
                a = linha.split(';')
                # Separa as informações dá página
                # numero;título do livro;conteúdo
                paginas.append([a[0], a[1], ' '.join(a[2:])])
            self.__livro = paginas
            arquivo.close()
        except FileNotFoundError:
            raise Exception("Livro não encontrado")

    def ler_pagina(self, n: int) -> Pagina:
        return Pagina(n, self.__livro[n][1], self.__livro[n][2])

    @staticmethod
    def get_livros() -> list[str]:
        """Retorna uma lista com os nomes dos livros disponíveis e seus arquivos"""
        for arquivo in os.listdir("livros"):
            if arquivo.endswith(".txt"):
                with open("livros/" + arquivo, "r") as f:
                    yield arquivo[:-4], f.readline().split(';')[1]

    def get_livro(self) -> list[Pagina]:
        return self.__livro