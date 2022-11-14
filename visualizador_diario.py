from visualizador import Visualizador
from controlador_diario import ControladorDiario
from controlador_texto_audio import ControladorTextoAudio
import tkinter as tk

class VisualizadorDiario(Visualizador):
    def __init__(self, usuario) -> None:
        super().__init__()
        self.root = tk.Tk()
        self.controlador_diario = ControladorDiario(usuario)
        self.controlador_diario.conectar()
        self.controlador_audio = ControladorTextoAudio()
    
    def renderizar_tela(self, textbox=None, contador=None):
        for text_line in textbox: text_line.delete(0, tk.END)
        if textbox:
            for line, text_line in zip(self.controlador_diario.ler_pagina(self.pagina_atual).texto, textbox):
                print(line)
                print(text_line)
                text_line.insert(tk.END, line)
        
        if contador: contador["text"]="Página " + str(self.pagina_atual+1) + " / " + str(len(self.controlador_diario.diario))
    
    def run(self):
        def voltar_pagina(textbox, contador):
            if self.pagina_atual > 0:
                self.pagina_anterior()
                self.renderizar_tela(textbox, contador)
            else:
                aviso = tk.Label(self.root, text="Você está na primeira página", fg="red")
                aviso.pack()
                self.root.after(2000, aviso.destroy)

        def avancar_pagina(textbox, contador):
            if self.pagina_atual <= len(self.controlador_diario.diario)-2:
                self.pagina_seguinte()
                self.renderizar_tela(textbox, contador)
            else:
                aviso = tk.Label(self.root, text="Você está na última página", fg="red")
                aviso.pack()
                self.root.after(2000, aviso.destroy)

        pagina = self.controlador_diario.ler_pagina(self.pagina_atual)
        self.root.geometry("1280x720")
        self.root.title(pagina.livro)

        T = tk.Label(
            self.root,
            text="Diário",
            font=("Arial", 20)
        )
        T.pack()

        textbox = [tk.Entry(self.root, justify=tk.LEFT, bg="white") for _ in range(10)]
        for text_line in textbox: text_line.pack()

        botoes = tk.Frame(self.root)
        botoes.pack()

        tk.Button(
            self.root,
            text="Anterior",
            command= lambda: voltar_pagina(textbox, contador) 
        ).pack(in_=botoes, side=tk.LEFT)

        tk.Button(
            self.root,
            text="Seguinte",
            command= lambda: avancar_pagina(textbox, contador)
        ).pack(in_=botoes, side=tk.RIGHT)

        contador = tk.Label(
            self.root,
            text="Página " + str(self.pagina_atual+1) + " / " + str(len(self.controlador_diario.diario))
        )
        contador.pack(in_=botoes, side=tk.BOTTOM)

        tk.Button(
            self.root,
            text="Ler",
            command= lambda: ControladorTextoAudio().ler_texto(pagina.texto)
        ).pack()

        self.renderizar_tela(textbox, contador)

        self.root.mainloop()