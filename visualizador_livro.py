import tkinter as tk

from visualizador import Visualizador
from controlador_livro import ControladorLivro
from controlador_texto_audio import ControladorTextoAudio

class VisualizadorLivro(Visualizador):
    def __init__(self, livro) -> None:
        super().__init__()
        # self.root = tk.Tk()
        self.controlador_livro = ControladorLivro()
        self.controlador_livro.conectar_livro(livro)
        self.controlador_audio = ControladorTextoAudio()

    def renderizar_tela(self, textbox=None, contador=None):
        if textbox: textbox["text"]=self.controlador_livro.ler_pagina(self.get_pagina_atual()).texto
        if contador: contador["text"]="Página " + str(self.pagina_atual+1) + " / " + str(len(self.controlador_livro.livro))

    def run(self, window=None):
        if not window: window = self.root
        
        # Comandos dos botões
        def voltar_pagina(textbox):
            if self.pagina_atual > 0:
                self.pagina_anterior()
                self.renderizar_tela(textbox, contador)
            else:
                aviso = tk.Label(window, text="Você está na primeira página", fg="red")
                aviso.pack()
                self.root.after(2000, aviso.destroy)

        def avancar_pagina(textbox):
            if self.pagina_atual <= len(self.controlador_livro.livro)-2:
                self.pagina_seguinte()
                self.renderizar_tela(textbox, contador)
            else:
                aviso = tk.Label(window, text="Você está na última página", fg="red")
                aviso.pack()
                self.root.after(2000, aviso.destroy)

        pagina = self.controlador_livro.ler_pagina(self.pagina_atual)
        window.geometry("1280x720")
        window.title(pagina.livro)
        
        T = tk.Label(
            window,
            text=pagina.livro,
            font=("Arial", 20)
        )
        T.pack()

        texto = tk.Label(
            window,
            text=pagina.texto,
            height=20,
            width=100,
            justify=tk.LEFT,
            wraplength=800,
            bg="white",
            )
        texto.pack()
        
        botoes_controle_pagina = tk.Frame(window)
        botoes_controle_pagina.pack()
        botoes_controle_audio = tk.Frame(window)
        botoes_controle_audio.pack()

        tk.Button(
            window,
            text="Anterior",
            command= lambda: voltar_pagina(texto) 
        ).pack(in_=botoes_controle_pagina, side=tk.LEFT)

        tk.Button(
            window,
            text="Seguinte",
            command= lambda: avancar_pagina(texto)
        ).pack(in_=botoes_controle_pagina, side=tk.RIGHT)

        contador = tk.Label(
            window,
            text="Página " + str(self.pagina_atual+1) + " / " + str(len(self.controlador_livro.livro))
        )
        contador.pack(in_=botoes_controle_pagina, side=tk.BOTTOM)

        tk.Button(
            window,
            text="Ler",
            command= lambda: ControladorTextoAudio().ler_texto(pagina.texto)
        ).pack(in_=botoes_controle_audio, side=tk.LEFT)

        tk.Button(
            window,
            text="Parar",
            command= lambda: ControladorTextoAudio().parar_leitura()
        ).pack(in_=botoes_controle_audio, side=tk.RIGHT)

        # if window == self.root: window.mainloop()

    def editar_pagina(self, pagina, texto):
        return "Você não pode editar uma página de um livro"
