import tkinter as tk
from visualizador_livro import VisualizadorLivro
from visualizador_diario import VisualizadorDiario
from visualizador import VisualizadorGerencia
from controlador_livro import ControladorLivro
from controlador_usuario import ControladorUsuario


class VisualizadorMenu(VisualizadorGerencia):
    def __init__(self, usuario: str, parent, root: tk.Tk = None) -> None:
        super().__init__(parent, root)
        # Atributos
        self.__usuario: str = usuario
        
        # Associações
        self.controlador_livro = ControladorLivro()
        self.controlador_usuario = ControladorUsuario()
        self.controlador_usuario.conectar_banco()

    def run(self):
        """Constrói a tela"""
        self.clear(self._root)
        self._root.geometry("1280x720")
        self._root.title("Menu")
        self.controlador_usuario.conectar_banco()

        tk.Label(
            self._root,
            text="Menu",
            font=("Arial", 20)
        ).pack()

        tk.Label(
            self._root,
            text="Escolha um livro",
            font=("Arial", 15)
        ).pack()
        
        # Livros
        # Cria um botão com o nome de cada livro cadastrado no sistema
        for arquivo, titulo in self.controlador_livro.get_livros():
            tk.Button(
                self._root,
                text=titulo,
                command=lambda: self.livro(arquivo),
                width=25
            ).pack()

        tk.Button(
            self._root,
            text="Diário",
            command=self.diario
        ).pack()

        tk.Label(
            self._root,
            text="Nome do usuário",
            font=("Arial", 15)
        ).pack()
        nome = tk.Entry(
            self._root,
            width=25
        )
        nome.pack()
        nome.insert(0, self.__usuario)

        nova_senha = tk.Entry(
            self._root,
            width=25
        )
        nova_senha.pack()

        confirmar_senha = tk.Entry(
            self._root,
            width=25
        )
        confirmar_senha.pack()

        tk.Button(
            self._root,
            text="Salvar alterações",
            command=lambda: self.salvar_alteracoes(nome.get(), nova_senha.get(), confirmar_senha.get())
        ).pack()

        tk.Button(
            self._root,
            text="Deletar conta",
            command=lambda: self.remover_usuario(self.__usuario)
        ).pack()

        if self._parent:
            tk.Button(
                self._root,
                text='Voltar',
                font=('Calibri', '12'),
                width=20,
                command=self._parent.run
            ).pack()

    def livro(self, livro: str) -> None:
        """Abre o livro escolhido e cria um botão para voltar ao menu"""
        self.clear(self._root)
        visualizador = VisualizadorLivro(livro, self, self._root)
        visualizador.run()

    def diario(self) -> None:
        """Abre o diário do usuário e cria um botão para voltar ao menu"""
        self.clear(self._root)
        visualizador = VisualizadorDiario(self.__usuario, self, self._root)
        visualizador.run()

    def salvar_alteracoes(self, nome: str, nova_senha: str, confirmar_senha: str) -> None:
        """Salva as alterações feitas no nome e na senha do usuário"""
        if nova_senha == confirmar_senha:
            usuario = self.controlador_usuario.buscar_usuario_por_nome(self.__usuario)
            if nova_senha: 
                nova_senha = self.hash_password(nova_senha, usuario.get_salt())
            else:
                nova_senha = usuario.get_salted_hash()
            self.controlador_usuario.atualizar_usuario(usuario.get_id(), nome, nova_senha)
            self.__usuario = nome
            self.run()
        else:
            tk.Label(
                self._root,
                text="As senhas não coincidem",
                font=("Arial", 15)
            ).pack()

    def remover_usuario(self, usuario: str) -> None:
        """Remove o usuário do sistema"""
        self.controlador_usuario.remover_usuario(usuario)
        self._parent.run()


if __name__ == "__main__":
    a = VisualizadorMenu("gabriel", None)
    a.run()
    a.get_root().mainloop()
