from tkinter import *

import tkinter as tk

 

class Application:

    def init (self, master = None):

 

        self.fonte = ("Verdana", "8")

 

 

        self.label = tk.Label (text = "FAZER LOGIN", font = ("Arial", 25, "italic", "bold"), foreground = "black", background = "cyan", width = 50, height =8)

        self.label.pack()

 

 

        self.container6 = Frame(master)

        self.container6["padx"] = 20

        self.container6["pady"] = 5

        self.container6.pack()

 

 

        self.container1 = Frame(master)

        self.container1["pady"] = 10

        self.container1.pack()       

 

        self.lblnome = tk.Label (text = "Email:", font=("Verdana", 18, "italic"), foreground = "black", background = "cyan", width = 50, height =20)

 

        self.lblnome.pack(side=LEFT)

 

        self.lblnome = tk.Label (text = "Senha:", font=("Verdana", 18, "italic"), foreground = "black", background = "cyan", width = 50, height =40)

 

        self.lblnome.pack(side=LEFT)

       

root = Tk()

 

root.geometry('900x700')

root.configure(background='cyan')

Application(root)

button

root.mainloop()