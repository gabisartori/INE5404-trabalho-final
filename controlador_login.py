from modelo_usuario import Usuario
import json

class ControladorLogin:
    def __init__(self) -> None:
        pass
    
    def verificar_senha(self, nome, salted_hash):
        with open("usuarios.json") as file:
            usuarios = json.load(file)
        for usuario in usuarios:
            if usuario['nome'] == nome and usuario['hash'] == salted_hash:
                return True
        return False