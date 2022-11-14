from pagina import Pagina
from visualizador_livro import VisualizadorLivro
from novo_visualizador import VisualizadorDiario

# livro = input("Digite o nome do livro: ")
livro = "coisa"

# a = int(input('livro ou diario? [1/2] '))

a = 2

if a == 1:
  visualizador = VisualizadorLivro(livro)
else:
  visualizador = VisualizadorDiario('gabriel')

visualizador.run()
