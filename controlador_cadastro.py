from modelo_usuario import Usuario
from controlador_usuario import ControladorUsuario

class ControladorCadastro(ControladorUsuario):
    def __init__(self, db="usuarios") -> None:
        super().__init__(db)
        self.conectar_banco()
        with open("contador.txt", "r") as file:
            self.contador_id = int(file.read())

    def cadastrar(self, nome, sal, senha_hash_sal):
        user = Usuario(self.contador_id, nome, sal, senha_hash_sal)
        self.contador_id += 1
        with open("contador.txt", "w") as file:
            file.write(str(self.contador_id))
        
        file = open("teste.txt", "a")
        file.write(f"{user.nome} {user.salt} {user.salted_hash}")
        file.write('\n')
        file.close()