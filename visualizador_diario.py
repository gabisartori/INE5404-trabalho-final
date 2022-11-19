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
        self.total_paginas = len(self.controlador_diario.diario)
    
    def renderizar_tela(self, textbox=None, contador=None):
        for text_line in textbox: text_line.delete(0, tk.END)
        if textbox:
            for line, text_line in zip(self.controlador_diario.ler_pagina(self.pagina_atual).texto, textbox):
                text_line.insert(tk.END, line)
        
        if contador: contador["text"]="Página " + str(self.pagina_atual+1) + " / " + str(self.total_paginas)
    
    def run(self):
        # Comandos dos botões
        def voltar_pagina(textbox, contador):
            if self.pagina_anterior():
                self.renderizar_tela(textbox, contador)
            else:
                self.aviso(self.root, "Você está na primeira página")

        def avancar_pagina(textbox, contador):
            if self.pagina_seguinte(self.total_paginas):
                self.renderizar_tela(textbox, contador)
            else:
                self.aviso(self.root, "Você está na última página")
    
        pagina = self.controlador_diario.ler_pagina(self.pagina_atual)
        self.root.geometry("1280x720")
        self.root.title(pagina.livro)

        tk.Label(
            self.root,
            text="Diário",
            font=("Arial", 20)
        ).pack()

        textbox = [tk.Entry(self.root, width=50, justify=tk.LEFT, bg="white") for _ in range(10)]
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
            text=f"Página {self.pagina_atual+1} / {len(self.controlador_diario.diario)}"
        )
        contador.pack(in_=botoes, side=tk.BOTTOM)

        tk.Button(
            self.root,
            text="Ler",
            command= lambda: ControladorTextoAudio().ler_texto(self.controlador_diario.ler_pagina(self.pagina_atual).texto)
        ).pack()

        tk.Button(
            self.root,
            text="Salvar",
            command= lambda: self.controlador_diario.salvar_pagina(self.pagina_atual, [text_line.get() for text_line in textbox])
        ).pack()

        self.renderizar_tela(textbox, contador)
        self.root.mainloop()