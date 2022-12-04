import tkinter as tk
from visualizador import VisualizadorGerencia
from controlador_cadastro import ControladorCadastro
import random


class VisualizadorCadastro(VisualizadorGerencia):
    def __init__(self, parent, root=None) -> None:
        super().__init__(parent, root)
        
        # Associações
        self.controlador = ControladorCadastro()
    
    def construir(self):
        """Constrói a tela"""
        self.limpar_tela()
        self._root.geometry("1280x720")

        tk.Label(
            self._root,
            text="Cadastro",
            font=("Calibri", 25, "bold"),
            foreground="black",
            width=50,
            height=8
        ).pack()

        tk.Label(
            self._root,
            text='Email:',
            font=('Bahnschrift Light SemiCondensed', 15, 'bold')
        ).pack()

        nome = tk.Entry(
            self._root,
            width=25,
            font=("Verdana", 18, "italic")
        )
        nome.pack()

        tk.Label(
            self._root,
            text='Senha:',
            font=('Bahnschrift Light SemiCondensed', 15, 'bold')
        ).pack()

        senha = tk.Entry(
            self._root,
            width=25,
            font=("Verdana", 18, "italic")
        )
        senha.pack()

        tk.Label(
            self._root,
            text='Confirma senha:',
            font=('Bahnschrift Light SemiCondensed', 15, 'bold')
        ).pack()

        confirma_senha = tk.Entry(
            self._root,
            width=25,
            font=("Verdana", 18, "italic")
        )
        confirma_senha.pack()

        tk.Button(
            self._root,
            text='Cadastrar',
            font=('Calibri', '12'),
            width=20,
            command=lambda: self.fazer_cadastro(nome.get(), senha.get(), confirma_senha.get())
            ).pack()

        if self._parent:
            tk.Button(
                self._root,
                text='Voltar',
                font=('Calibri', '12'),
                width=20,
                command=self._parent.construir
            ).pack()

    def fazer_cadastro(self, nome: str, senha: str, confirma: str) -> None:
        """Verifica se o cadastro é válido e passa os valores para o controlador de cadastro"""
        
        # Verifica se os campos foram preenchidos corretamente
        if not nome or not senha or not confirma:
            self.aviso("Preencha todos os campos!")
            return
        if senha != confirma:
            self.aviso("As senhas devem ser iguais!")
            return
        
        # Realiza o cadastro
        sal = str(random.randint(1, 1_000_000))
        cadastro = self.controlador.cadastrar_usuario(nome, sal, self.hash_senha(senha, sal))
        
        # Verifica se o cadastro foi bem sucedido
        if isinstance(cadastro, str):
            self.aviso(cadastro)
        else:
            self.aviso("Cadastro realizado com sucesso!", "green")
