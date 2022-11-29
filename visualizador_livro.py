import tkinter as tk

from visualizador import Visualizador
from controlador_livro import ControladorLivro
from controlador_texto_audio import ControladorTextoAudio

class VisualizadorLivro(Visualizador):
    def __init__(self, livro, root=None) -> None:
        super().__init__(root)
        self.controlador_livro = ControladorLivro()
        self.controlador_livro.conectar_livro(livro)
        self.controlador_audio = ControladorTextoAudio()
        self.total_paginas = len(self.controlador_livro.livro)

    def renderizar_tela(self, textbox=None, contador=None) -> None:
        '''Recarrega componentes da tela que podem ser alterados'''
        if textbox: textbox["text"]=self.controlador_livro.ler_pagina(self.get_pagina_atual()).texto
        if contador: contador["text"]=f"Página {self.pagina_atual+1} / {self.total_paginas}"

    def run(self) -> None:
        '''Constroi a tela e inicia o loop'''
        
        # Comandos dos botões
        def voltar_pagina(textbox):
            if self.pagina_anterior():
                self.renderizar_tela(textbox, contador)
            else:
                self.aviso(self.root, "Você está na primeira página")

        def avancar_pagina(textbox):
            if self.pagina_seguinte(self.total_paginas):
                self.renderizar_tela(textbox, contador)
            else:
                self.aviso(self.root, "Você está na última página")

        # Carrega a primeira página do livro
        pagina = self.controlador_livro.ler_pagina(self.pagina_atual)
        self.root.geometry("1280x720")
        self.root.title(pagina.livro)
        
        # Título da janela
        T = tk.Label(
            self.root,
            text=pagina.livro,
            font=("Arial", 20)
        )
        T.pack()

        # Texto da página 
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
        
        # Containers para alinhar os botões
        botoes_controle_pagina = tk.Frame(self.root)
        botoes_controle_pagina.pack()
        botoes_controle_audio = tk.Frame(self.root)
        botoes_controle_audio.pack()

        # Botões de controle de página
        tk.Button(
            self.root,
            text="Anterior",
            command= lambda: voltar_pagina(texto) 
        ).pack(in_=botoes_controle_pagina, side=tk.LEFT)

        tk.Button(
            self.root,
            text="Seguinte",
            command= lambda: avancar_pagina(texto)
        ).pack(in_=botoes_controle_pagina, side=tk.RIGHT)

        contador = tk.Label(
            self.root,
            text=f"Página {self.pagina_atual+1} / {self.total_paginas}"
        )
        contador.pack(in_=botoes_controle_pagina, side=tk.BOTTOM)

        # Botões de controle de áudio
        tk.Button(
            self.root,
            text="Ler",
            command= lambda: ControladorTextoAudio().ler_texto(self.controlador_livro.ler_pagina(self.pagina_atual).texto)
        ).pack(in_=botoes_controle_audio, side=tk.LEFT)

        tk.Button(
            self.root,
            text="Parar",
            command= lambda: ControladorTextoAudio().parar_leitura()
        ).pack(in_=botoes_controle_audio, side=tk.RIGHT)


    def editar_pagina(self, pagina: int, texto: str) -> str:
        return "Você não pode editar uma página de um livro"
