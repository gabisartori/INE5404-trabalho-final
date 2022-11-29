from modelo_usuario import Usuario
from controlador_usuario import ControladorUsuario

class ControladorLogin(ControladorUsuario):
    def __init__(self, db="usuarios") -> None:
        super().__init__(db)
        self.conectar_banco()
    
    def verificar_senha(self, nome, salted_hash):
        usuario = self.buscar_usuario_por_nome(nome)
        if isinstance(usuario, str):
            return False
        if usuario.salted_hash == salted_hash:
            return True
