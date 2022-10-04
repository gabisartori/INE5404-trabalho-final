from visualizador import Visualizador


class VisualizadorLivro(Visualizador):
    def __init__(self, pagina_atual) -> None:
        super().__init__(pagina_atual)
    
    def editar_pagina(self, pagina, texto):
        return "Você não pode editar uma página de um livro"