import tkinter as tk

class Visualizador:
    def __init__(self, root=None) -> None:
        self.pagina_atual: int = 0
        self.total_paginas: int = 0
        
        # Permite que os objetos sejam usados tanto como uma janela em si ou como um componente
        self.root: tk.Tk = root if root else tk.Tk()

    @staticmethod    
    def clear(window) -> None:
        '''Remove todo o conteúdo de uma janela'''
        for widget in window.winfo_children():
            widget.destroy()


    def get_pagina_atual(self) -> int:
        return self.pagina_atual

    def set_pagina_atual(self, pagina) -> None:
        self.pagina_atual = pagina

    def pagina_anterior(self) -> bool:
        '''Tenta voltar uma página, retorna True se a página atual não for a primeira'''
        if self.pagina_atual > 0:
            self.pagina_atual -= 1
            return True
        return False
    
    def pagina_seguinte(self, total_paginas) -> bool:
        '''Tenta avançar uma página, retorna True se a página atual não for a última'''
        if self.pagina_atual < total_paginas - 1:
            self.pagina_atual += 1
            return True
        return False
    
    def editar_pagina(self, pagina, texto) -> None:
        '''\o/'''
        print("Página do que?")
    
    def aviso(self, window, texto) -> None:
        '''Exibe uma mensagem em vermelho no fim da tela'''
        aviso = tk.Label(window, text=texto, fg="red")
        aviso.pack()
        window.after(2000, aviso.destroy)
    
    @staticmethod
    def update_texto(textbox: dict, new_text: str) -> None:
        '''Atualiza o item "text" de um dicionário'''
        textbox["text"] = new_text