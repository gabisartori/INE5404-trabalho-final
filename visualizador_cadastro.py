import tkinter as tk
from visualizador import Visualizador
from controlador_login import ControladorLogin

class VisualizadorCadastro(Visualizador):
    def __init__(self, root=None) -> None:
        super().__init__(root)
        self.controlador_login = ControladorLogin()
    
    def run(self):
        self.clear(self.root)

        tk.Label(
            self.root,
            text="Cadastro",
            font=("Calibri", 25, "bold"),
            foreground="black",
            width=50,
            height=8
        ).pack()

        tk.Label(
            self.root,
            text='Email:',
            font=('Bahnschrift Light SemiCondensed', 15, 'bold')
        ).pack()

        nome = tk.Entry(
            self.root,
            width=25,
            font=("Verdana", 18, "italic")
        )
        nome.pack()

        tk.Label(
            self.root,
            text='Senha:',
            font=('Bahnschrift Light SemiCondensed', 15, 'bold')
        ).pack()

        senha = tk.Entry(
            self.root,
            width=25,
            font=("Verdana", 18, "italic")
        )
        senha.pack()

        tk.Label(
            self.root,
            text='Confirma senha:',
            font=('Bahnschrift Light SemiCondensed', 15, 'bold')
        ).pack()

        confirma_senha = tk.Entry(
            self.root,
            width=25,
            font=("Verdana", 18, "italic")
        )
        confirma_senha.pack()

        tk.Button(
            self.root,
            text='Cadastrar',
            font=('Calibri', '12'),
            width=20,
            command=lambda: self.faz_cadastro(nome.get(), senha.get(), confirma_senha.get())
            ).pack()
    
    def faz_cadastro(self, nome, senha, confirma):
        self.run()

        if senha == confirma:
            self.controlador_login.cadastrar(nome, senha)

            confirmar = tk.Label(self.root, text='Cadastro concluído com sucesso!', font=(
                'Bahnschrift Light SemiCondensed', 15, 'bold'), fg='green')
            confirmar.pack()
            self.root.after(2000, confirmar.destroy)

        else:
            confirmar = tk.Label(
                self.root,
                text='As senhas devem ser iguais!',
                font=('Bahnschrift Light SemiCondensed', 15, 'bold'),
                fg='red'
            )
            confirmar.pack()

            self.root.after(2000, confirmar.destroy)