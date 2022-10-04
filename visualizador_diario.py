from visualizador import Visualizador

class VisualizadorDiario(Visualizador):
    def __init__(self, pagina_atual) -> None:
        super().__init__(pagina_atual)
    
    def editar_pagina(self, pagina, texto):
        pagina.texto = texto