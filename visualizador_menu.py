import tkinter as tk
from visualizador_livro import VisualizadorLivro
from visualizador_diario import VisualizadorDiario
from visualizador import Visualizador
from controlador_livro import ControladorLivro
from controlador_usuario import ControladorUsuario

class VisualizadorMenu(Visualizador):
    def __init__(self, usuario: str, parent, root: tk.Tk=None) -> None:
        super().__init__(parent, root)
        self.usuario: str = usuario
        self.controlador_livro = ControladorLivro()
        self.controlador_usuario = ControladorUsuario()
        self.controlador_usuario.conectar_banco()

    def run(self):
        """Constrói a tela"""
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

        tk.Button(
            self.root,
            text="Deletar conta",
            command=lambda: self.controlador_usuario.remover_usuario(self.usuario)
        ).pack()

        if self.parent:
            tk.Button(
                self.root,
                text='Voltar',
                font=('Calibri', '12'),
                width=20,
                command=self.parent.run
            ).pack()


    def livro(self, livro: str) -> None:
        """Abre o livro escolhido e cria um botão para voltar ao menu"""
        self.clear(self.root)
        visualizador = VisualizadorLivro(livro, self, self.root)
        visualizador.run()

    def diario(self) -> None:
        """Abre o diário do usuário e cria um botão para voltar ao menu"""
        self.clear(self.root)
        visualizador = VisualizadorDiario(self.usuario, self, self.root)
        visualizador.run()

if __name__ == "__main__":
    a= VisualizadorMenu("gabriel")
    a.run()
    a.root.mainloop()