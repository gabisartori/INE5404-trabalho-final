class Pagina:
    def __init__(self, numero: int, livro: str, texto: str or list[str]) -> None:
        self.__numero: int = numero
        self.__livro: str = livro
        self._texto: str or list[str] = texto

    def get_numero(self) -> int:
        return self.__numero
    
    def get_livro(self) -> str:
        return self.__livro
    
    def get_texto(self) -> str or list[str]:
        return self._texto
    
    def set_texto(self, texto: str or list[str]) -> None:
        self._texto = texto


class PaginaDiario(Pagina):
    def __init__(self, numero: int, livro: str, texto: str or list[str]) -> None:
        super().__init__(numero, livro, texto)
        if isinstance(texto, str):
            self._texto = texto.split('\n')

        while len(self._texto) < 10:
            self._texto.append('')
