import tkinter as tk
from visualizador import VisualizadorGerencia
from visualizador_cadastro import VisualizadorCadastro
from visualizador_menu import VisualizadorMenu
from controlador_login import ControladorLogin


class VisualizadorLogin(VisualizadorGerencia):

    def __init__(self, parent, root=None):
        super().__init__(parent, root)
        
        # Associações
        self.controlador_login = ControladorLogin()

    def run(self):
        """Constrói a tela"""
        self.clear(self._root)
        self._root.geometry("1280x720")

        self.controlador_login.conectar_banco()

        tk.Label(
            text="Menu",
            font=("Calibri", 25, "bold"),
            foreground="black",
            width=50,
            height=8).pack()

        tk.Label(
            self._root,
            text='Email:',
            font=('Bahnschrift Light SemiCondensed', 15, 'bold')
        ).pack()

        nome = tk.Entry(self._root, width=25, font=("Verdana", 18, "italic"))
        nome.pack()

        tk.Label(
            self._root,
            text='Senha:',
            font=('Bahnschrift Light SemiCondensed', 15, 'bold')
        ).pack()

        senha = tk.Entry(self._root, width=25, font=("Verdana", 18, "italic"))
        senha.pack()
        senha["show"] = "*"

        tk.Button(
            self._root,
            text='Entrar',
            font=('Calibri', '12'),
            width=20,
            command=lambda: self.login(nome.get(), senha.get())
        ).pack()

        tk.Button(
            self._root,
            text='Cadastrar-se',
            font=('Calibri', '12'),
            width=20,
            command=self.tela_cadastro
        ).pack()

        if self._parent:
            tk.Button(
                self._root,
                text='Voltar',
                font=('Calibri', '12'),
                width=20,
                command=self._parent.run
            ).pack()

    def login(self, nome: str, senha: str) -> None:
        """Verifica se o usuário existe e se a senha está correta, caso esteja, abre o menu do usuário"""
        # Busca pelo usuário no banco de dados
        usuario = self.controlador_login.buscar_usuario_por_nome(nome)

        # Caso a busca por um usário não tenha retornado uma mensagem de erro
        if not isinstance(usuario, str):
            salted_hash = self.hash_password(senha, usuario.get_salt())
            if usuario.get_salted_hash() == salted_hash:
                self.tela_menu(nome)
            else:
                confirmar = tk.Label(
                    self._root,
                    text='Senha incorreta!',
                    font=('Bahnschrift Light SemiCondensed', 15, 'bold'),
                    fg='green'
                )
                confirmar.pack()
                self._root.after(2000, confirmar.destroy)
        # Caso a busca por um usário tenha retornado uma mensagem de erro
        else:
            confirmar = tk.Label(
                self._root,
                text=usuario,
                font=('Bahnschrift Light SemiCondensed', 15, 'bold'),
                fg='green'
            )
            confirmar.pack()
            self._root.after(2000, confirmar.destroy)

    def tela_cadastro(self) -> None:
        """Contrói a tela de cadastro na janela atual, e um botão para voltar ao começo"""
        self.clear(self._root)
        VisualizadorCadastro(self, self._root).run()
        
    def tela_menu(self, usuario) -> None:
        """Contrói a tela de menu na janela atual, e um botão para voltar ao começo"""
        self.clear(self._root)
        VisualizadorMenu(usuario, self, self._root).run()


if __name__ == "__main__":
    a = VisualizadorLogin(None)
    a.run()
    a._root.mainloop()
