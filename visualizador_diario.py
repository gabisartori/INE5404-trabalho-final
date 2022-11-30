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
        self.total_paginas = len(self.controlador_diario.diario)
    
    def renderizar_tela(self, textbox=None, contador=None) -> None:
        """Recarrega componentes da tela que podem ser alterados"""
        for text_line in textbox:
            text_line.delete(0, tk.END)
        if textbox:
            for line, text_line in zip(self.controlador_diario.ler_pagina(self.pagina_atual).texto, textbox):
                text_line.insert(tk.END, line)
        
        if contador:
            contador["text"] = f"Página {self.pagina_atual+1} / {len(self.controlador_diario.diario)}"
    
    def run(self) -> None:
        """Constroi a tela"""
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
    
        # Carrega a primeira página do diário
        pagina = self.controlador_diario.ler_pagina(self.pagina_atual)
        self.root.geometry("1280x720")
        self.root.title(pagina.livro)

        # Título da janela
        tk.Label(
            self.root,
            text="Diário",
            font=("Arial", 20)
        ).pack()

        # Constrói as linhas de texto
        textbox = [tk.Entry(self.root, width=50, justify=tk.LEFT, bg="white") for _ in range(10)]
        for text_line in textbox:
            text_line.pack()

        botoes = tk.Frame(self.root)
        botoes.pack()

        # Controle de página
        tk.Button(
            self.root,
            text="Anterior",
            command=lambda: voltar_pagina(textbox, contador)
        ).pack(in_=botoes, side=tk.LEFT)

        tk.Button(
            self.root,
            text="Seguinte",
            command=lambda: avancar_pagina(textbox, contador)
        ).pack(in_=botoes, side=tk.RIGHT)

        contador = tk.Label(
            self.root,
            text=f"Página {self.pagina_atual+1} / {len(self.controlador_diario.diario)}"
        )
        contador.pack(in_=botoes, side=tk.BOTTOM)
        
        botoes_controle_audio = tk.Frame(self.root)
        botoes_controle_audio.pack()
        
        # Controle de áudio
        tk.Button(
            self.root,
            text="Ler",
            command=lambda: self.controlador_audio.ler_texto(
                self.controlador_diario.ler_pagina(self.pagina_atual).texto
            )
        ).pack(in_=botoes_controle_audio, side=tk.LEFT)

        tk.Button(
            self.root,
            text="Parar",
            command=lambda: self.controlador_audio.parar_leitura()
        ).pack(in_=botoes_controle_audio, side=tk.RIGHT)

        # Salvar alterações da página
        tk.Button(
            self.root,
            text="Salvar",
            command=lambda: self.controlador_diario.salvar_pagina(
                self.pagina_atual,
                [text_line.get() for text_line in textbox]
            )
        ).pack()

        if self.parent:
            tk.Button(
                self.root,
                text='Voltar',
                font=('Calibri', '12'),
                width=20,
                command=self.parent.run
            ).pack()

        # Carrega a página pela primeira vez
        self.renderizar_tela(textbox, contador)
