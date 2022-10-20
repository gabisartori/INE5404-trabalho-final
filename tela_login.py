from tkinter import *
import tkinter as tk
import pygame

pygame.init()

while True:
    

    class Application:

        def __init__ (self, master = None):
            
            self.fonte = ("Verdana", "8")
            self.label = tk.Label (text = "FAZER LOGIN", font = ("Arial", 25, "italic", "bold"), foreground = "black", background = "#62c9de", width = 50, height =8)
            self.label.pack()

            self.container3 = Frame(master)
            self.container3["padx"] = 180
            self.container3.pack()

            self.container6 = Frame(master)
            self.container6["padx"] = 20
            self.container6["pady"] = 5
            self.container6.pack()

            self.container2 = Frame(master)
            self.container2["padx"] = 20
            self.container2.pack()
            
            self.container4 = Frame(master)
            self.container4["padx"] = 20
            self.container4["pady"] = 50
            self.container4.pack()

            self.container1 = Frame(master)
            self.container1["pady"] = 10
            self.container1.pack()       


            #adicionar informacoes

            self.nome = Entry(self.container2)
            self.nome["width"] = 25
            self.nome["font"] = "Verdana", 18, "italic"
            self.nome.pack(side=LEFT)


            self.nome = Entry(self.container4)
            self.nome["width"] = 25
            self.nome["font"] = "Verdana", 18, "italic"
            self.nome.pack(side= LEFT)
            

    root = Tk()


    root.geometry('900x700')
    root.configure(background="#62c9de")
    Application(root)

    root.mainloop()


'''
            self.lblnome = tk.Label (text = "Email:", font=("Verdana", 18, "italic"), foreground = "black", background = "#62c9de", width = 30, height =10)
            self.lblnome.pack(side=LEFT)
            self.lblnome = tk.Label (text = "Senha:", font=("Verdana", 18, "italic"), foreground = "black", background = "#62c9de", width = 30, height =40) 
            self.lblnome.pack(side=LEFT)
            
'''
