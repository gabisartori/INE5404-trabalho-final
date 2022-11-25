from visualizador import Visualizador
from controlador_diario import ControladorDiario
from controlador_texto_audio import ControladorTextoAudio
import tkinter as tk

class VisualizadorDiario(Visualizador):
    def __init__(self, usuario, root=None) -> None:
        super().__init__(root)
        self.controlador_diario = ControladorDiario(usuario)
        self.controlador_diario.conectar()
        self.controlador_audio = ControladorTextoAudio()
        self.total_paginas = len(self.controlador_diario.diario)
    
    def renderizar_tela(self, textbox=None, contador=None):
        for text_line in textbox: text_line.delete(0, tk.END)
        if textbox:
            for line, text_line in zip(self.controlador_diario.ler_pagina(self.pagina_atual).texto, textbox):
                text_line.insert(tk.END, line)
        
        if contador: contador["text"]=f"Página {self.pagina_atual+1} / {len(self.controlador_diario.diario)}"
    
    def run(self, window=None):
        if not window: window = self.root
        # Comandos dos botões
        def voltar_pagina(textbox, contador):
            if self.pagina_anterior():
                self.renderizar_tela(textbox, contador)
            else:
                self.aviso(window, "Você está na primeira página")

        def avancar_pagina(textbox, contador):
            if self.pagina_seguinte(self.total_paginas):
                self.renderizar_tela(textbox, contador)
            else:
                self.aviso(window, "Você está na última página")
    
        pagina = self.controlador_diario.ler_pagina(self.pagina_atual)
        window.geometry("1280x720")
        window.title(pagina.livro)

        tk.Label(
            window,
            text="Diário",
            font=("Arial", 20)
        ).pack()

        textbox = [tk.Entry(window, width=50, justify=tk.LEFT, bg="white") for _ in range(10)]
        for text_line in textbox: text_line.pack()

        botoes = tk.Frame(window)
        botoes.pack()

        tk.Button(
            window,
            text="Anterior",
            command= lambda: voltar_pagina(textbox, contador) 
        ).pack(in_=botoes, side=tk.LEFT)

        tk.Button(
            window,
            text="Seguinte",
            command= lambda: avancar_pagina(textbox, contador)
        ).pack(in_=botoes, side=tk.RIGHT)

        contador = tk.Label(
            window,
            text=f"Página {self.pagina_atual+1} / {len(self.controlador_diario.diario)}"
        )
        contador.pack(in_=botoes, side=tk.BOTTOM)
        
        botoes_controle_audio = tk.Frame(window)
        botoes_controle_audio.pack()
        
        tk.Button(
            window,
            text="Ler",
            command= lambda: ControladorTextoAudio().ler_texto(self.controlador_diario.ler_pagina(self.pagina_atual).texto)
        ).pack(in_=botoes_controle_audio, side=tk.LEFT)

        tk.Button(
            window,
            text="Parar",
            command= lambda: ControladorTextoAudio().parar_leitura()
        ).pack(in_=botoes_controle_audio, side=tk.RIGHT)

        tk.Button(
            window,
            text="Salvar",
            command= lambda: self.controlador_diario.salvar_pagina(self.pagina_atual, [text_line.get() for text_line in textbox])
        ).pack()

        self.renderizar_tela(textbox, contador)
        # if window == self.root: window.mainloop()