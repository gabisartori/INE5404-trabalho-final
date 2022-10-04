class Visualizador:
    def __init__(self, pagina_atual) -> None:
        self.pagina_atual = pagina_atual
    
    def pagina_anterior(self):
        self.pagina_atual -= 1
    
    def pagina_seguinte(self):
        self.pagina_atual += 1
    
    def pagina_especifica(self, pagina):
        self.pagina_atual = pagina
    
    def editar_pagina(self, pagina, texto):
        print("Página do que? ")