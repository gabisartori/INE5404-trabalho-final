import tkinter as tk

from visualizador import VisualizadorLeitura
from controlador_livro import ControladorLivro
from controlador_texto_audio import ControladorTextoAudio


class VisualizadorLivro(VisualizadorLeitura):
    def __init__(self, livro, parent, root=None) -> None:
        super().__init__(parent, root)
        self.controlador_livro = ControladorLivro()
        self.controlador_livro.conectar_livro(livro)
        self.controlador_audio = ControladorTextoAudio()
        self.set_total_paginas(len(self.controlador_livro.get_livro()))

    def construir(self) -> None:
        """Constroi a tela e inicia o loop"""
        
        # Comandos dos botões
        def voltar_pagina(textbox):
            if self.pagina_anterior():
                self.renderizar_tela(textbox, contador)
            else:
                self.aviso("Você está na primeira página")

        def avancar_pagina(textbox):
            if self.pagina_seguinte(self.get_total_paginas()):
                self.renderizar_tela(textbox, contador)
            else:
                self.aviso("Você está na última página")

        # Carrega a primeira página do livro
        pagina = self.controlador_livro.ler_pagina(self.get_pagina_atual())
        self._root.geometry("1280x720")
        self._root.title(pagina.get_livro())
        
        # Título da janela
        tk.Label(
            self._root,
            text=pagina.get_livro(),
            font=("Arial", 20)
        ).pack()

        # Texto da página 
        texto = tk.Label(
            self._root,
            text=pagina.get_texto(),
            height=20,
            width=100,
            justify=tk.LEFT,
            wraplength=800,
            bg="white",
            )
        texto.pack()
        
        # Containers para alinhar os botões
        botoes_controle_pagina = tk.Frame(self._root)
        botoes_controle_pagina.pack()
        botoes_controle_audio = tk.Frame(self._root)
        botoes_controle_audio.pack()

        # Botões de controle de página
        tk.Button(
            self._root,
            text="Anterior",
            command=lambda: voltar_pagina(texto)
        ).pack(in_=botoes_controle_pagina, side=tk.LEFT)

        tk.Button(
            self._root,
            text="Seguinte",
            command=lambda: avancar_pagina(texto)
        ).pack(in_=botoes_controle_pagina, side=tk.RIGHT)

        contador = tk.Label(
            self._root,
            text=f"Página {self.get_pagina_atual()+1} / {self.get_total_paginas()}"
        )
        contador.pack(in_=botoes_controle_pagina, side=tk.BOTTOM)

        # Botões de controle de áudio
        tk.Button(
            self._root,
            text="Ler",
            command=lambda: ControladorTextoAudio().ler_texto(
                self.controlador_livro.ler_pagina(self.get_pagina_atual()).get_texto()
            )
        ).pack(in_=botoes_controle_audio, side=tk.LEFT)

        tk.Button(
            self._root,
            text="Parar",
            command=lambda: ControladorTextoAudio().parar_leitura()
        ).pack(in_=botoes_controle_audio, side=tk.RIGHT)

        if self._parent:
            tk.Button(
                self._root,
                text='Voltar',
                font=('Calibri', '12'),
                width=20,
                command=self._parent.construir
            ).pack()

    def renderizar_tela(self, textbox=None, contador=None) -> None:
            """Recarrega componentes da tela que podem ser alterados"""
            if textbox:
                textbox["text"] = self.controlador_livro.ler_pagina(self.get_pagina_atual()).get_texto()
            if contador:
                contador["text"] = f"Página {self.get_pagina_atual()+1} / {self.get_total_paginas()}"
