from tkinter import *
import tkinter as tk

class Application:

    def __init__ (self, master):
        for widget in master.winfo_children():
            widget.destroy()    
        
        self.label = tk.Label (text = "Menu", font = ("Calibri", 25, "bold"), foreground = "black", width = 50, height =8)
        self.label.pack()

        self.label_email = Label (master, text = 'Email:', font = ('Bahnschrift Light SemiCondensed', 15,'bold'))
        self.label_email.pack()

        self.nome = Entry(master, width = 25, font = ("Verdana", 18, "italic"))
        self.nome.pack()
        
        self.label_senha = Label (master, text = 'Senha:', font = ('Bahnschrift Light SemiCondensed', 15,'bold'))
        self.label_senha.pack()
        
        self.senha = Entry(master, width = 25, font = ("Verdana", 18, "italic"))
        self.senha.pack()
        #self.senha["show"] = "*"


        self.entrar = Button(master, text = 'Entrar', font = ('Calibri','12'),width = 20, command = lambda: self.verificaSenha(master, self.nome.get(),self.senha.get()))
        self.entrar.pack()

        self.entrar = Button(master, text = 'Cadastrar-se', font = ('Calibri','12'),width = 20, command = lambda : self.cadastro(master))
        self.entrar.pack()


    def cadastro(self,master):
        for widget in master.winfo_children():
            widget.destroy()
            
        
        self.label = tk.Label (text = "Cadastro", font = ("Calibri", 25, "bold"), foreground = "black", width = 50, height =8)
        self.label.pack()

        self.label_email = Label (master, text = 'Email:', font = ('Bahnschrift Light SemiCondensed', 15,'bold'))
        self.label_email.pack()

        self.nome = Entry(master, width = 25, font = ("Verdana", 18, "italic"))
        self.nome.pack()
        
        self.label_senha = Label (master, text = 'Senha:', font = ('Bahnschrift Light SemiCondensed', 15,'bold'))
        self.label_senha.pack()
        
        self.senha = Entry(master, width = 25, font = ("Verdana", 18, "italic"))
        self.senha.pack()
        
        self.label_senha = Label (master, text = 'Confirma senha:', font = ('Bahnschrift Light SemiCondensed', 15,'bold'))
        self.label_senha.pack()              
            
        self.confirma_senha= Entry(master, width = 25, font = ("Verdana", 18, "italic"))
        self.confirma_senha.pack()


        self.entrar = Button(master, text = 'Cadastrar', font = ('Calibri','12'),width = 20, command = lambda : self.faz_cadastro(master, self.nome.get(),self.senha.get(),self.confirma_senha.get()))
        self.entrar.pack()
        
        self.voltar = Button(master, text = 'Voltar', font = ('Calibri','12'),width = 20, command = lambda : self.__init__(master))
        self.voltar.pack()    
        
    def faz_cadastro(self,master, nome, senha, confirma):
        self.cadastro(master)

        if senha == confirma:
            file = open("teste.txt","a")
            file.write(str(nome + ' ' + senha))
            file.write('\n')
            file.close()
                       
            self.confirmar = Label (master, text= 'Cadastro concluído com sucesso!', font =('Bahnschrift Light SemiCondensed', 15,'bold'),fg='green')
            self.confirmar.pack()
            master.after(2000, self.confirmar.destroy)
            
            
        else:
            
            self.confirmar = Label (master, text= 'As senhas devem ser iguais!', font =('Bahnschrift Light SemiCondensed', 15,'bold'),fg='red')
            self.confirmar.pack()
                        

    def verificaSenha(self,master,nome,senha):
        
        file = open("teste.txt","r")
        texto = file.readlines()
        flag = False
        for linha1 in texto:
            if str(nome + ' ' + senha) in linha1:
                print('achei')
                self.confirmar = Label (master, text= 'Usuário autenticado!', font =('Bahnschrift Light SemiCondensed', 15,'bold'),fg='green')
                self.confirmar.pack()
                flag = True
                break
        if flag == False:
            print('nao achei')
            self.confirmar = Label (master, text= 'Erro de autenticação!', font =('Bahnschrift Light SemiCondensed', 15,'bold'),fg='green')
            self.confirmar.pack()

        file.close()            
            

root = Tk()
root.geometry('900x700')
Application(root)
root.mainloop()

