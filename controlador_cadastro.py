from modelo_usuario import Usuario

class ControladorCadastro:
    def __init__(self) -> None:
        with open("contador.txt", "r") as file:
            self.contador_id = int(file.read())

    def cadastrar(self, nome, senha):
        user = Usuario(self.contador_id, nome, senha)
        self.contador_id += 1
        with open("contador.txt", "w") as file:
            file.write(str(self.contador_id))
        
        file = open("teste.txt", "a")
        file.write(f"{user.nome} {user.salt} {user.salted_hash}")
        file.write('\n')
        file.close()