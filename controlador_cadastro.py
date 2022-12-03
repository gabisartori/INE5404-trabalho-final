from modelo_usuario import Usuario
from controlador_usuario import ControladorUsuario
import json 


class ControladorCadastro(ControladorUsuario):
    def __init__(self, db: str = "usuarios") -> None:
        super().__init__(db)
        self.conectar_banco()
        try:
            with open("contador.txt") as arquivo:
                self.__contador_id = int(arquivo.read())
        except FileNotFoundError:
            with open("contador.txt", 'w') as arquivo:
                arquivo.write("1")
            self.__contador_id = 1

    def cadastrar_usuario(self, nome: str, sal: str, hash_salteada: str) -> Usuario | str:
        """Recebe os dados do usuário, cria um objeto do tipo Usuario e o adiciona ao banco de dados"""
        usuario = Usuario(self.__contador_id, nome, sal, hash_salteada)

        # Incrementa o contador de id
        self.__contador_id += 1
        with open("contador.txt", "w") as arquivo:
            arquivo.write(str(self.__contador_id))
        
        self.get_usuarios().append({
            'id': self.__contador_id,
            'nome': nome,
            'sal': sal,
            'hash_salteada': hash_salteada
            })
        
        with open(f'{self.get_db()}.json', 'w') as arquivo:
            json.dump(self.get_usuarios(), arquivo)

        return usuario
