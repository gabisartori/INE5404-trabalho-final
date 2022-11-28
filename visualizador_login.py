import tkinter as tk
from visualizador import Visualizador


class VisualizadorLogin(Visualizador):

    def __init__(self, root=None):
        super().__init__(root)

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
            command=lambda: self.cadastro(self.root)
        ).pack()

    def cadastro(self):
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
            command=lambda: self.faz_cadastro(nome.get(), senha.get(), confirma_senha.get()))

        tk.Button(
            self.root,
            text='Voltar',
            font=('Calibri', '12'),
            width=20,
            command=lambda: self.__init__(self.root)
        ).pack()

    def faz_cadastro(self, nome, senha, confirma):
        self.cadastro(self.root)

        if senha == confirma:
            file = open("teste.txt", "a")
            file.write(str(nome + ' ' + senha))
            file.write('\n')
            file.close()

            self.confirmar = tk.Label(self.root, text='Cadastro concluído com sucesso!', font=(
                'Bahnschrift Light SemiCondensed', 15, 'bold'), fg='green')
            self.confirmar.pack()
            self.root.after(2000, self.confirmar.destroy)

        else:
            confirmar = tk.Label(self.root,
                                 text='As senhas devem ser iguais!',
                                 font=('Bahnschrift Light SemiCondensed',
                                       15, 'bold'),
                                 fg='red'
                                 ).pack()

            self.root.after(2000, confirmar.destroy)

    def verificaSenha(self, nome, senha):

        file = open("teste.txt", "r")
        texto = file.readlines()
        flag = False
        for linha1 in texto:
            if str(nome + ' ' + senha) in linha1:
                print('achei')
                tk.Label(
                    self.root,
                    text='Usuário autenticado!',
                    font=('Bahnschrift Light SemiCondensed', 15, 'bold'),
                    fg='green'
                ).pack()
                self.root.after(2000, self.confirmar.destroy)

                flag = True
                break
        if flag == False:
            print('nao achei')
            confirmar = tk.Label(
                self.root,
                text='Erro de autenticação!',
                font=('Bahnschrift Light SemiCondensed', 15, 'bold'),
                fg='green'
            ).pack()
            self.root.after(2000, confirmar.destroy)

        file.close()


root = tk.Tk()
root.geometry('900x700')
a = VisualizadorLogin(root)
a.run()
root.mainloop()
