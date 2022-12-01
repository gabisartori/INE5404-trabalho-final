from modelo_usuario import Usuario
from controlador_usuario import ControladorUsuario


class ControladorCadastro(ControladorUsuario):
    def __init__(self, db: str = "usuarios") -> None:
        super().__init__(db)
        self.conectar_banco()
        with open("contador.txt", "r") as file:
            self.contador_id = int(file.read())

    def cadastrar_usuario(self, nome: str, sal: str, senha_hash_sal: str) -> Usuario | str:
        """Recebe os dados do usuário, cria um objeto do tipo Usuario e o adiciona ao banco de dados"""
        usuario = Usuario(self.contador_id, nome, sal, senha_hash_sal)

        # Incrementa o contador de id
        self.contador_id += 1
        with open("contador.txt", "w") as file:
            file.write(str(self.contador_id))

        # Parte a ser reescrita usando json

        lista = [{'id':self.contador_id,'nome': nome,'salted': sal,'salted_hash': senha_hash_sal}][:]
        with open('usuarios.json','w') as outfile:
            json.dump(lista.copy(),outfile)

        return usuario
