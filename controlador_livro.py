from modelo_pagina import Pagina
import os

class ControladorLivro:
    def __init__(self) -> None:
        self.livro: list[Pagina] = []
    
    def conectar_livro(self, livro: str) -> None:
        '''Carrega o conteúdo do livro'''
        try:
            file = open("livros/" + livro + ".txt", "r")
            conteudo = file.readlines()
            paginas = []
            for linha in conteudo:
                a = linha.split(';')
                # Separa as informações dá página
                # numero;título do livro;conteúdo
                paginas.append([a[0], a[1], ' '.join(a[2:])])
            self.livro = paginas
        except FileNotFoundError:
            raise Exception("Livro não encontrado")

    def ler_pagina(self, n: int) -> Pagina:
        return Pagina(n, self.livro[n][1], self.livro[n][2])
    
    def get_livros(self) -> list[str]:
        '''Retorna uma lista com os nomes dos livros disponíveis e seus arquivos'''
        for arquivo in os.listdir("livros"):
            if arquivo.endswith(".txt"):
                with open("livros/" + arquivo, "r") as f:
                    yield arquivo[:-4], f.readline().split(';')[1]