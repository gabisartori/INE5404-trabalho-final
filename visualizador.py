import tkinter as tk

class Visualizador:
    def __init__(self, root=None) -> None:
        self.pagina_atual = 0
        self.total_paginas = 0
        self.root = root if root else tk.Tk()

    @staticmethod    
    def clear(window):
        for widget in window.winfo_children():
            widget.destroy()


    def get_pagina_atual(self):
        return self.pagina_atual

    def set_pagina_atual(self, pagina):
        self.pagina_atual = pagina

    def pagina_anterior(self):
        if self.pagina_atual > 0:
            self.pagina_atual -= 1
            return True
        return False
    
    def pagina_seguinte(self, total_paginas):
        if self.pagina_atual < total_paginas - 1:
            self.pagina_atual += 1
            return True
        return False
    
    def editar_pagina(self, pagina, texto):
        print("Página do que?")
    
    def aviso(self, window, texto):
        aviso = tk.Label(window, text=texto, fg="red")
        aviso.pack()
        window.after(2000, aviso.destroy)
    
    @staticmethod
    def update_texto(textbox, new_text):
        textbox["text"] = new_text