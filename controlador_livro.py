from modelo_pagina import Pagina

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