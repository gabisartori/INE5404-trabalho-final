from visualizador import VisualizadorLeitura
from controlador_diario import ControladorDiario
from controlador_texto_audio import ControladorTextoAudio
import tkinter as tk


class VisualizadorDiario(VisualizadorLeitura):
    def __init__(self, usuario: str, parent, root: VisualizadorLeitura | tk.Tk | None) -> None:
        super().__init__(parent, root)
        self.controlador_diario = ControladorDiario(usuario)
        self.controlador_audio = ControladorTextoAudio()
        self.controlador_diario.conectar()
        self.set_total_paginas(len(self.controlador_diario.get_diario()))
    
    def renderizar_tela(self, textbox=None, contador=None) -> None:
        """Recarrega componentes da tela que podem ser alterados"""
        for text_line in textbox:
            text_line.delete(0, tk.END)
        if textbox:
            for line, text_line in zip(self.controlador_diario.ler_pagina(self.get_pagina_atual()).get_texto(), textbox):
                text_line.insert(tk.END, line)
        
        if contador:
            contador["text"] = f"Página {self.get_pagina_atual()+1} / {self.get_total_paginas()}"
    
    def run(self) -> None:
        """Constroi a tela"""
        # Comandos dos botões
        def voltar_pagina(textbox, contador):
            if self.pagina_anterior():
                self.renderizar_tela(textbox, contador)
            else:
                self.aviso(self._root, "Você está na primeira página")

        def avancar_pagina(textbox, contador):
            if self.pagina_seguinte(self.get_total_paginas()):
                self.renderizar_tela(textbox, contador)
            else:
                self.aviso(self._root, "Você está na última página")
    
        # Carrega a primeira página do diário
        pagina = self.controlador_diario.ler_pagina(self.get_pagina_atual())
        self._root.geometry("1280x720")
        self._root.title(pagina.get_livro())

        # Título da janela
        tk.Label(
            self._root,
            text="Diário",
            font=("Arial", 20)
        ).pack()

        # Constrói as linhas de texto
        textbox = [tk.Entry(self._root, width=50, justify=tk.LEFT, bg="white") for _ in range(10)]
        for text_line in textbox:
            text_line.pack()

        botoes = tk.Frame(self._root)
        botoes.pack()

        # Controle de página
        tk.Button(
            self._root,
            text="Anterior",
            command=lambda: voltar_pagina(textbox, contador)
        ).pack(in_=botoes, side=tk.LEFT)

        tk.Button(
            self._root,
            text="Seguinte",
            command=lambda: avancar_pagina(textbox, contador)
        ).pack(in_=botoes, side=tk.RIGHT)

        contador = tk.Label(
            self._root,
            text=f"Página {self.get_pagina_atual()+1} / {self.get_total_paginas()}"
        )
        contador.pack(in_=botoes, side=tk.BOTTOM)
        
        botoes_controle_audio = tk.Frame(self._root)
        botoes_controle_audio.pack()
        
        # Controle de áudio
        tk.Button(
            self._root,
            text="Ler",
            command=lambda: self.controlador_audio.ler_texto(
                self.controlador_diario.ler_pagina(self.get_pagina_atual()).get_texto()
            )
        ).pack(in_=botoes_controle_audio, side=tk.LEFT)

        tk.Button(
            self._root,
            text="Parar",
            command=lambda: self.controlador_audio.parar_leitura()
        ).pack(in_=botoes_controle_audio, side=tk.RIGHT)

        # Salvar alterações da página
        tk.Button(
            self._root,
            text="Salvar",
            command=lambda: self.controlador_diario.salvar_pagina(
                self.get_pagina_atual(),
                [text_line.get() for text_line in textbox]
            )
        ).pack()

        if self._parent:
            tk.Button(
                self._root,
                text='Voltar',
                font=('Calibri', '12'),
                width=20,
                command=self._parent.run
            ).pack()

        # Carrega a página pela primeira vez
        self.renderizar_tela(textbox, contador)
