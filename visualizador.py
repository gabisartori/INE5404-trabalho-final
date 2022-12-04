import tkinter as tk
import hashlib


class Visualizador:
    def __init__(self, parent, root=None) -> None:
        self.set_parent(parent)
        # Permite que os objetos sejam usados tanto como uma janela em si ou como um componente
        self._root: tk.Tk = root if root else tk.Tk()
    
    def get_parent(self):
        return self._parent
    
    def set_parent(self, parent):
        self._parent = parent
    
    def get_root(self):
        return self._root
    
    def set_root(self, root):
        self._root = root

    def aviso(self, texto: str, cor="red") -> None:
        """Exibe uma mensagem em vermelho no fim da tela"""
        aviso = tk.Label(self._root, text=texto, fg=cor, font=('Bahnschrift Light SemiCondensed', 15, 'bold'))
        aviso.pack()
        self._root.after(2000, aviso.destroy)
    
 
    def limpar_tela(self) -> None:
        """Remove todo o conteúdo de uma janela"""
        for widget in self._root.winfo_children():
            widget.destroy()
    
    @staticmethod
    def atualizar_texto(textbox: dict, new_text: str) -> None:
        """Atualiza o item "text" de um dicionário"""
        textbox["text"] = new_text


class VisualizadorGerencia(Visualizador):
    def __init__(self, parent, root=None) -> None:
        super().__init__(parent, root)
    
    @staticmethod
    def hash_senha(password: str, salt: str):
        return hashlib.sha256((password + salt).encode()).hexdigest()


class VisualizadorLeitura(Visualizador):
    def __init__(self, parent, root=None) -> None:
        super().__init__(parent, root)
        self._pagina_atual: int = 0
        self._total_paginas: int = 0
    
    def get_pagina_atual(self) -> int:
        return self._pagina_atual

    def set_pagina_atual(self, pagina: int) -> None:
        self._pagina_atual = pagina

    def get_total_paginas(self) -> int:
        return self._total_paginas
    
    def set_total_paginas(self, total: int) -> None:
        self._total_paginas = total

    def pagina_anterior(self) -> bool:
        """Tenta voltar uma página, retorna True se a página atual não for a primeira"""
        if self._pagina_atual > 0:
            self._pagina_atual -= 1
            return True
        return False
    
    def pagina_seguinte(self, total_paginas: int) -> bool:
        """Tenta avançar uma página, retorna True se a página atual não for a última"""
        if self._pagina_atual < total_paginas - 1:
            self._pagina_atual += 1
            return True
        return False
