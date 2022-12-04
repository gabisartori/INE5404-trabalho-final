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

    def construir(self):
        """Constrói a tela"""
        self.limpar_tela()
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
            def call_book(arquivo=arquivo):
                return lambda: self.tela_livro(arquivo)
            
            tk.Button(
                self._root,
                text=titulo,
                command=call_book(),
                width=25
            ).pack()

        tk.Button(
            self._root,
            text="Diário",
            command=self.tela_diario
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
                command=self._parent.construir
            ).pack()

    def tela_livro(self, livro: str) -> None:
        """Abre o livro escolhido e cria um botão para voltar ao menu"""
        self.limpar_tela()
        visualizador = VisualizadorLivro(livro, self, self._root)
        visualizador.construir()

    def tela_diario(self) -> None:
        """Abre o diário do usuário e cria um botão para voltar ao menu"""
        self.limpar_tela()
        visualizador = VisualizadorDiario(self.__usuario, self, self._root)
        visualizador.construir()

    def salvar_alteracoes(self, nome: str, nova_senha: str, confirmar_senha: str) -> None:
        """Salva as alterações feitas no nome e na senha do usuário"""
        if nova_senha == confirmar_senha:
            usuario = self.controlador_usuario.buscar_usuario_por_nome(self.__usuario)
            if nova_senha: 
                nova_senha = self.hash_senha(nova_senha, usuario.get_sal())
            else:
                nova_senha = usuario.get_hash_salteada()
            a = self.controlador_usuario.atualizar_usuario(usuario.get_id(), nome, nova_senha)
            if type(a) == str:
                self.aviso(a)
            self.__usuario = nome
            self.construir()
        else:
            self.aviso("As senhas devem ser iguais!")

    def remover_usuario(self, usuario: str) -> None:
        """Remove o usuário do sistema"""
        self.controlador_usuario.remover_usuario(usuario)
        self._parent.construir()


if __name__ == "__main__":
    a = VisualizadorMenu("gabriel", None)
    a.construir()
    a.get_root().mainloop()
