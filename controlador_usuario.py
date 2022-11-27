from modelo_usuario import Usuario

class ControladorUsuario:
    def __init__(self, db) -> None:
        self.db = db
    
    def conectar_banco(self, db) -> None:
        pass

    def buscar_usuario_por_id(self, id) -> Usuario:
        pass

    def buscar_usuario_por_email(self, email) -> Usuario:
        pass

    def cadastrar_usuario(self, usuario) -> Usuario or str:
        pass

    def atualizar_usuario(self, id, usuario) -> Usuario or str:
        pass

    def remover_usuario(self, id) -> Usuario or str:
        pass
