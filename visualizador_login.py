import tkinter as tk
from visualizador import Visualizador
from visualizador_cadastro import VisualizadorCadastro
from visualizador_menu import VisualizadorMenu
from controlador_login import ControladorLogin


class VisualizadorLogin(Visualizador):

    def __init__(self, root=None):
        super().__init__(root)
        self.controlador_login = ControladorLogin()

    def run(self):
        self.clear(self.root)

        tk.Label(
            text="Menu",
            font=("Calibri", 25, "bold"),
            foreground="black",
            width=50,
            height=8).pack()

        tk.Label(
            self.root,
            text='Email:',
            font=('Bahnschrift Light SemiCondensed', 15, 'bold')
        ).pack()

        nome = tk.Entry(self.root, width=25, font=("Verdana", 18, "italic"))
        nome.pack()

        tk.Label(
            self.root,
            text='Senha:',
            font=('Bahnschrift Light SemiCondensed', 15, 'bold')
        ).pack()

        senha = tk.Entry(self.root, width=25, font=("Verdana", 18, "italic"))
        senha.pack()
        senha["show"] = "*"

        tk.Button(
            self.root,
            text='Entrar',
            font=('Calibri', '12'),
            width=20,
            command=lambda: self.verificaSenha(nome.get(), senha.get())
        ).pack()

        tk.Button(
            self.root,
            text='Cadastrar-se',
            font=('Calibri', '12'),
            width=20,
            command=self.tela_cadastro
        ).pack()

    def verificaSenha(self, nome, senha):
        if self.controlador_login.verificar_senha(nome, senha):
            self.tela_menu(nome)
        else:
            confirmar = tk.Label(
                self.root,
                text='Erro de autenticação!',
                font=('Bahnschrift Light SemiCondensed', 15, 'bold'),
                fg='green'
            ).pack()
            self.root.after(2000, confirmar.destroy)

    def tela_cadastro(self):
        self.clear(self.root)
        VisualizadorCadastro(self.root).run()
        tk.Button(
            self.root,
            text='Voltar',
            font=('Calibri', '12'),
            width=20,
            command=self.run
        ).pack()
    
    def tela_menu(self, usuario):
        self.clear(self.root)
        VisualizadorMenu(usuario, self.root).inicio()
        tk.Button(
            self.root,
            text='Voltar',
            font=('Calibri', '12'),
            width=20,
            command=self.run
        ).pack()

a = VisualizadorLogin()
a.run()
a.root.mainloop()
