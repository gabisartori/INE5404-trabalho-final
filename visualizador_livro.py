import tkinter as tk

from visualizador import Visualizador
from controlador_livro import ControladorLivro

class VisualizadorLivro(Visualizador):
    def __init__(self, livro) -> None:
        super().__init__()
        self.root = tk.Tk()
        self.controlador = ControladorLivro()
        self.controlador.conectar_livro(livro)

    def renderizar_tela(self, textbox=None, contador=None):
        if textbox: textbox["text"]=self.controlador.ler_pagina(self.get_pagina_atual()).texto
        if contador: contador["text"]="Página " + str(self.pagina_atual+1) + " / " + str(len(self.controlador.livro))

    def run(self):
        def voltar_pagina(textbox):
            if self.pagina_atual > 0:
                self.pagina_anterior()
                self.renderizar_tela(textbox, contador)
            else:
                aviso = tk.Label(self.root, text="Você está na primeira página", fg="red")
                aviso.pack()
                self.root.after(2000, aviso.destroy)

        def avancar_pagina(textbox):
            if self.pagina_atual <= len(self.controlador.livro)-2:
                self.pagina_seguinte()
                self.renderizar_tela(textbox, contador)
            else:
                aviso = tk.Label(self.root, text="Você está na última página", fg="red")
                aviso.pack()
                self.root.after(2000, aviso.destroy)

        pagina = self.controlador.ler_pagina(self.pagina_atual)
        self.root.geometry("1280x720")
        self.root.title(pagina.livro)
        
        T = tk.Label(
            self.root,
            text=pagina.livro,
            font=("Arial", 20)
        )
        T.pack()

        texto = tk.Label(
            self.root,
            text=pagina.texto,
            height=20,
            width=100,
            justify=tk.LEFT,
            wraplength=800,
            bg="white",
            )
        texto.pack()
        
        botoes = tk.Frame(self.root)
        botoes.pack()

        tk.Button(
            self.root,
            text="Anterior",
            command= lambda: voltar_pagina(texto) 
        ).pack(in_=botoes, side=tk.LEFT)

        tk.Button(
            self.root,
            text="Seguinte",
            command= lambda: avancar_pagina(texto)
        ).pack(in_=botoes, side=tk.RIGHT)

        contador = tk.Label(
            self.root,
            text="Página " + str(self.pagina_atual+1) + " / " + str(len(self.controlador.livro))
        )
        contador.pack(in_=botoes, side=tk.BOTTOM)

        self.root.mainloop()

    def editar_pagina(self, pagina, texto):
        return "Você não pode editar uma página de um livro"
