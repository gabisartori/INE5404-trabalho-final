import tkinter as tk

from visualizador import Visualizador
from controlador_livro import ControladorLivro

class VisualizadorLivro(Visualizador):
    def __init__(self, livro) -> None:
        super().__init__()
        self.root = tk.Tk()
        self.controlador = ControladorLivro()
        self.controlador.conectar_livro(livro)

    def run(self):
        pagina = self.controlador.ler_pagina(self.pagina_atual)
        self.root.geometry("1000x1000")
        self.root.title(pagina.livro)
        T = tk.Label(self.root, text=pagina.texto, width=500, height=500)
        T.pack()
        self.root.mainloop()

    def editar_pagina(self, pagina, texto):
        return "Você não pode editar uma página de um livro"
