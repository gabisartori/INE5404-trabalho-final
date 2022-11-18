class Visualizador:
    def __init__(self) -> None:
        self.pagina_atual = 0
    
    def get_pagina_atual(self):
        return self.pagina_atual

    def set_pagina_atual(self, pagina):
        self.pagina_atual = pagina

    def pagina_anterior(self):
        self.pagina_atual -= 1
    
    def pagina_seguinte(self):
        self.pagina_atual += 1
    
    def editar_pagina(self, pagina, texto):
        print("Página do que?")
    
    @staticmethod
    def update_texto(textbox, new_text):
        textbox["text"] = new_text