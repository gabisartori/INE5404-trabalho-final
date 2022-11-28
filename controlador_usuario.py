from modelo_usuario import Usuario
import json


class ControladorUsuario:
    def __init__(self, db) -> None:
        self.db = db
        self.usuarios = None

    def conectar_banco(self) -> None:
        with open(f"{self.db}.json") as file:
            self.usuarios = json.load(file)

    def buscar_usuario_por_id(self, id) -> Usuario:
        pass

    def cadastrar_usuario(self, usuario) -> Usuario or str:
        pass

    def atualizar_usuario(self, id, usuario) -> Usuario or str:
        pass

    def remover_usuario(self, id) -> Usuario or str:
        pass
