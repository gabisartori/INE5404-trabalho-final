import tkinter as tk
from visualizador_livro import VisualizadorLivro
from visualizador_diario import VisualizadorDiario

def clear(window):
    for widget in window.winfo_children():
        widget.destroy()

def inicio():
    clear(root)
    root.geometry("1280x720")
    root.title("Diário")

    tk.Label(
        root,
        text="Menu",
        font=("Arial", 20)
    ).pack()

    tk.Button(
        root,
        text="Livro",
        command=livro
    ).pack()

    tk.Button(
        root,
        text="Diário",
        command=diario
    ).pack()

def livro():
    clear(root)
    visualizador = VisualizadorLivro("coisa")
    visualizador.run(root)
    tk.Button(root, text="voltar", command=inicio).pack()


def diario():
    clear(root)
    visualizador = VisualizadorDiario('gabriel')
    visualizador.run(root)
    tk.Button(root, text="voltar", command=inicio).pack()

root = tk.Tk()
root.geometry("1280x720")
root.title("Menu")

inicio()
root.mainloop()