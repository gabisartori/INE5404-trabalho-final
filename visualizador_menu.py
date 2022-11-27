import tkinter as tk
from visualizador_livro import VisualizadorLivro
from visualizador_diario import VisualizadorDiario
from visualizador import Visualizador
from controlador_livro import ControladorLivro

class Menu(Visualizador):
    def __init__(self, usuario: str, root: tk.Tk =None) -> None:
        super().__init__(root)
        self.usuario: str = usuario
        self.controlador_livro = ControladorLivro()

    def inicio(self):
        self.clear(self.root)
        self.root.geometry("1280x720")
        self.root.title("Menu")

        tk.Label(
            self.root,
            text="Menu",
            font=("Arial", 20)
        ).pack()

        tk.Label(
            self.root,
            text="Escolha um livro",
            font=("Arial", 15)
        ).pack()
        
        # Livros
        # Cria um botão com o nome de cada livro cadastrado no sistema
        for arquivo, titulo in self.controlador_livro.get_livros():
            tk.Button(
                self.root,
                text=titulo,
                command=lambda : self.livro(arquivo),
                width=25
            ).pack()

        tk.Button(
            self.root,
            text="Diário",
            command=self.diario
        ).pack()

    def livro(self, livro: str):
        self.clear(self.root)
        visualizador = VisualizadorLivro(livro, self.root)
        visualizador.run(self.root)
        tk.Button(self.root, text="voltar", command=self.inicio).pack()


    def diario(self):
        self.clear(self.root)
        visualizador = VisualizadorDiario(self.usuario, self.root)
        visualizador.run(self.root)
        tk.Button(self.root, text="voltar", command=self.inicio).pack()

a= Menu("gabriel")
a.inicio()
a.root.mainloop()