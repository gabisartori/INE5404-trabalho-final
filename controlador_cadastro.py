from modelo_usuario import Usuario
from controlador_usuario import ControladorUsuario
import json 

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

        with open('usuarios.json') as file:
            usuarios = json.load(file)
        
        usuarios.append({'id':self.contador_id,'nome': nome,'salt': sal,'salted_hash': senha_hash_sal})
        print(usuarios)
        with open('usuarios.json','w') as file:
            json.dump(usuarios,file)

        return usuario
