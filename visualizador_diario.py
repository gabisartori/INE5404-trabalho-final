from visualizador import Visualizador
from controlador_diario import ControladorDiario
from controlador_texto_audio import ControladorTextoAudio
import tkinter as tk

class VisualizadorDiario(Visualizador):
    def __init__(self, pagina_atual) -> None:
        super().__init__(pagina_atual)
        self.root = tk.Tk()
        self.controladordiario = ControladorDiario()
        self.controlador_audio = ControladorTextoAudio()
    
    def editar_pagina(self, pagina, texto):
        pagina.texto = texto
    
    def run(self):
        pagina = self.controladordiario.ler_pagina(self.pagina_atual)
        self.root.geometry("1280x720")
        self.root.title(pagina.livro)
        
        T = tk.Label(
            self.root,
            text="Diário",
            font=("Arial", 20)
        )
        T.pack()

        texto = tk.Label(
            self.root,
            text=pagina.texto,
            height=20,
            width=100,
            justify=tk.LEFT,
            wraplength=800,
            bg="white",
            )
        texto.pack()
        
        botoes = tk.Frame(self.root)
        botoes.pack()

        tk.Button(
            self.root,
            text="Anterior",
            command= lambda: voltar_pagina(texto) 
        ).pack(in_=botoes, side=tk.LEFT)

        tk.Button(
            self.root,
            text="Seguinte",
            command= lambda: avancar_pagina(texto)
        ).pack(in_=botoes, side=tk.RIGHT)

        contador = tk.Label(
            self.root,
            text="Página " + str(self.pagina_atual+1) + " / " + str(len(self.controlador_livro.livro))
        )
        contador.pack(in_=botoes, side=tk.BOTTOM)

        tk.Button(
            self.root,
            text="Ler",
            command= lambda: ControladorTextoAudio().ler_texto(pagina.texto)
        ).pack()

        self.root.mainloop()