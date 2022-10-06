from pagina import Pagina

class ControladorLivro:
    def __init__(self):
        self.livro = []
    
    def conectar_livro(self, livro):
        try:
            file = open("livros/" + livro + ".txt", "r")
            conteudo = file.readlines()
            paginas = []
            for linha in conteudo:
                a = linha.split()
                paginas.append([a[0], a[1], ' '.join(a[2:])])
            self.livro = paginas
        except FileNotFoundError:
            print("Livro não encontrado")

    def ler_pagina(self, n):
        return Pagina(n, self.livro[n][1], self.livro[n][2])