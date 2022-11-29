import tkinter as tk
from visualizador import Visualizador
from visualizador_cadastro import VisualizadorCadastro
from visualizador_menu import VisualizadorMenu
from controlador_login import ControladorLogin
from controlador_usuario import ControladorUsuario
import hashlib

def hash_password(password: str, salt: str):
    return hashlib.sha256((password + salt).encode()).hexdigest()

class VisualizadorLogin(Visualizador):

    def __init__(self, root=None):
        super().__init__(root)
        self.controlador_login = ControladorLogin()
        self.controlador_usuario = ControladorUsuario("usuarios")
        self.controlador_usuario.conectar_banco()

    def run(self):
        """Constrói a tela"""
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
            command=lambda: self.login(nome.get(), senha.get())
        ).pack()

        tk.Button(
            self.root,
            text='Cadastrar-se',
            font=('Calibri', '12'),
            width=20,
            command=self.tela_cadastro
        ).pack()

    def login(self, nome: str, senha: str) -> None:
        """Verifica se o usuário existe e se a senha está correta, caso esteja, abre o menu do usuário"""
        # Busca pelo usuário no banco de dados
        usuario = self.controlador_login.buscar_usuario_por_nome(nome)

        # Caso a busca por um usário não tenha retornado uma mensagem de erro
        if not isinstance(usuario, str):
            salted_hash = hash_password(senha, usuario.salt)
            if usuario.salted_hash == salted_hash:
                self.tela_menu(nome)
            else:
                confirmar = tk.Label(
                    self.root,
                    text='Senha incorreta!',
                    font=('Bahnschrift Light SemiCondensed', 15, 'bold'),
                    fg='green'
                )
                confirmar.pack()
                self.root.after(2000, confirmar.destroy)
        # Caso a busca por um usário tenha retornado uma mensagem de erro
        else:
            confirmar = tk.Label(
                self.root,
                text=usuario,
                font=('Bahnschrift Light SemiCondensed', 15, 'bold'),
                fg='green'
            )
            confirmar.pack()
            self.root.after(2000, confirmar.destroy)


    def tela_cadastro(self) -> None:
        """Contrói a tela de cadastro na janela atual, e um botão para voltar ao começo"""
        self.clear(self.root)
        VisualizadorCadastro(self.root).run()
        tk.Button(
            self.root,
            text='Voltar',
            font=('Calibri', '12'),
            width=20,
            command=self.run
        ).pack()
    
    def tela_menu(self, usuario) -> None:
        """Contrói a tela de menu na janela atual, e um botão para voltar ao começo"""
        self.clear(self.root)
        VisualizadorMenu(usuario, self.root).run()
        tk.Button(
            self.root,
            text='Voltar',
            font=('Calibri', '12'),
            width=20,
            command=self.run
        ).pack()

if __name__ == "__main__":
    a = VisualizadorLogin()
    a.run()
    a.root.mainloop()
