from pagina import Pagina
from visualizador_livro import VisualizadorLivro

livro = input("Digite o nome do livro: ")

visualizador = VisualizadorLivro(livro)

visualizador.run()