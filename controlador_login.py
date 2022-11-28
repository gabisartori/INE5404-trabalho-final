import json
import random
import hashlib

class ControladorLogin:
    def __init__(self) -> None:
        pass

    def cadastrar(self, nome, senha):
        file = open("teste.txt", "a")
        sal = str(random.randint(1, 1_000_000))
        salted_hash = hashlib.sha256((senha + sal).encode()).hexdigest()
        file.write(f"{nome} {sal} {salted_hash}")
        file.write('\n')
        file.close()
    
    def verificar_senha(self, nome, salted_hash):
        with open("usuarios.json") as file:
            usuarios = json.load(file)
        for usuario in usuarios:
            if usuario['nome'] == nome and usuario['hash'] == salted_hash:
                return True
        return False