import tkinter as tk
from visualizador import Visualizador

class VisualizadorLogin(Visualizador):

    def __init__ (self):
        pass
    def run(self):
        self.clear(self.root)    
        
        self.label = tk.Label (text = "Menu", font = ("Calibri", 25, "bold"), foreground = "black", width = 50, height =8)
        self.label.pack()

        self.label_email = tk.Label (self.root, text = 'Email:', font = ('Bahnschrift Light SemiCondensed', 15,'bold'))
        self.label_email.pack()

        self.nome = tk.Entry(self.root, width = 25, font = ("Verdana", 18, "italic"))
        self.nome.pack()
        
        self.label_senha = tk.Label (self.root, text = 'Senha:', font = ('Bahnschrift Light SemiCondensed', 15,'bold'))
        self.label_senha.pack()
        
        self.senha = tk.Entry(self.root, width = 25, font = ("Verdana", 18, "italic"))
        self.senha.pack()
        #self.senha["show"] = "*"


        self.entrar = tk.Button(self.root, text = 'Entrar', font = ('Calibri','12'),width = 20, command = lambda: self.verificaSenha(self.root, self.nome.get(),self.senha.get()))
        self.entrar.pack()

        self.entrar = tk.Button(self.root, text = 'Cadastrar-se', font = ('Calibri','12'),width = 20, command = lambda : self.cadastro(self.root))
        self.entrar.pack()


    def cadastro(self):
        self.clear(self.root)
            
        
        self.label = tk.Label (text = "Cadastro", font = ("Calibri", 25, "bold"), foreground = "black", width = 50, height =8)
        self.label.pack()

        self.label_email = tk.Label (self.root, text = 'Email:', font = ('Bahnschrift Light SemiCondensed', 15,'bold'))
        self.label_email.pack()

        self.nome = tk.Entry(self.root, width = 25, font = ("Verdana", 18, "italic"))
        self.nome.pack()
        
        self.label_senha = tk.Label (self.root, text = 'Senha:', font = ('Bahnschrift Light SemiCondensed', 15,'bold'))
        self.label_senha.pack()
        
        self.senha = tk.Entry(self.root, width = 25, font = ("Verdana", 18, "italic"))
        self.senha.pack()
        
        self.label_senha = tk.Label (self.root, text = 'Confirma senha:', font = ('Bahnschrift Light SemiCondensed', 15,'bold'))
        self.label_senha.pack()              
            
        self.confirma_senha= tk.Entry(self.root, width = 25, font = ("Verdana", 18, "italic"))
        self.confirma_senha.pack()


        self.entrar = tk.Button(self.root, text = 'Cadastrar', font = ('Calibri','12'),width = 20, command = lambda : self.faz_cadastro(self.root, self.nome.get(),self.senha.get(),self.confirma_senha.get()))
        self.entrar.pack()
        
        self.voltar = tk.Button(self.root, text = 'Voltar', font = ('Calibri','12'),width = 20, command = lambda : self.__init__(self.root))
        self.voltar.pack()    
        
    def faz_cadastro(self, nome, senha, confirma):
        self.cadastro(self.root)

        if senha == confirma:
            file = open("teste.txt","a")
            file.write(str(nome + ' ' + senha))
            file.write('\n')
            file.close()
                       
            self.confirmar = tk.Label (self.root, text= 'Cadastro concluído com sucesso!', font =('Bahnschrift Light SemiCondensed', 15,'bold'),fg='green')
            self.confirmar.pack()
            self.root.after(2000, self.confirmar.destroy)
            
            
        else:
            
            self.confirmar = tk.Label (self.root, text= 'As senhas devem ser iguais!', font =('Bahnschrift Light SemiCondensed', 15,'bold'),fg='red')
            self.confirmar.pack()
            self.root.after(2000, self.confirmar.destroy)
                        

    def verificaSenha(self, nome, senha):
        
        file = open("teste.txt","r")
        texto = file.readlines()
        flag = False
        for linha1 in texto:
            if str(nome + ' ' + senha) in linha1:
                print('achei')
                self.confirmar = tk.Label (self.root, text= 'Usuário autenticado!', font =('Bahnschrift Light SemiCondensed', 15,'bold'),fg='green')
                self.confirmar.pack()
                self.root.after(2000, self.confirmar.destroy)

                flag = True
                break
        if flag == False:
            print('nao achei')
            self.confirmar = tk.Label (self.root, text= 'Erro de autenticação!', font =('Bahnschrift Light SemiCondensed', 15,'bold'),fg='green')
            self.confirmar.pack()
            self.root.after(2000, self.confirmar.destroy)


        file.close()            
            

root = tk.Tk()
root.geometry('900x700')
VisualizadorLogin(root)
root.mainloop()

