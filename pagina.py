class Pagina:
    def __init__(self, numero, livro, texto):
        self.numero = numero
        self.livro = livro
        self.texto = texto


class PaginaDiario(Pagina):
    def __init__(self, numero, livro, texto):
        super().__init__(numero, livro, texto)
        while len(self.texto) < 10:
            self.texto.append('')