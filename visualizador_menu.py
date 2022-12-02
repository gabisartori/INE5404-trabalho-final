import tkinter as tk
from visualizador_livro import VisualizadorLivro
from visualizador_diario import VisualizadorDiario
from visualizador import VisualizadorGerencia
from controlador_livro import ControladorLivro
from controlador_usuario import ControladorUsuario


class VisualizadorMenu(VisualizadorGerencia):
    def __init__(self, usuario: str, parent, root: tk.Tk = None) -> None:
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
        self.controlador_usuario.conectar_banco()

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
                command=lambda: self.livro(arquivo),
                width=25
            ).pack()

        tk.Button(
            self.root,
            text="Diário",
            command=self.diario
        ).pack()

        tk.Label(
            self.root,
            text="Nome do usuário",
            font=("Arial", 15)
        ).pack()
        nome = tk.Entry(
            self.root,
            width=25
        )
        nome.pack()
        nome.insert(0, self.usuario)

        nova_senha = tk.Entry(
            self.root,
            width=25
        )
        nova_senha.pack()

        confirmar_senha = tk.Entry(
            self.root,
            width=25
        )
        confirmar_senha.pack()

        tk.Button(
            self.root,
            text="Salvar alterações",
            command=lambda: self.salvar_alteracoes(nome.get(), nova_senha.get(), confirmar_senha.get())
        ).pack()

        tk.Button(
            self.root,
            text="Deletar conta",
            command=lambda: self.remover_usuario(self.usuario)
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

    def salvar_alteracoes(self, nome: str, nova_senha: str, confirmar_senha: str) -> None:
        """Salva as alterações feitas no nome e na senha do usuário"""
        if nova_senha == confirmar_senha:
            usuario = self.controlador_usuario.buscar_usuario_por_nome(self.usuario)
            if nova_senha: 
                nova_senha = self.hash_password(nova_senha, usuario.salt)
            else:
                nova_senha = usuario.salted_hash
            self.controlador_usuario.atualizar_usuario(usuario.id, nome, nova_senha)
            self.usuario = nome
            self.run()
        else:
            tk.Label(
                self.root,
                text="As senhas não coincidem",
                font=("Arial", 15)
            ).pack()

    def remover_usuario(self, usuario: str) -> None:
        """Remove o usuário do sistema"""
        self.controlador_usuario.remover_usuario(usuario)
        self.parent.run()

if __name__ == "__main__":
    a = VisualizadorMenu("gabriel", None)
    a.run()
    a.root.mainloop()
