class Pagina:
    def __init__(self, numero: int, livro: str, texto: str or list[str]) -> None:
        self.numero: int = numero
        self.livro: str = livro
        self.texto: str or list[str] = texto


class PaginaDiario(Pagina):
    def __init__(self, numero: int, livro: str, texto: str or list[str]) -> None:
        super().__init__(numero, livro, texto)
        while len(self.texto) < 10:
            self.texto.append('')
