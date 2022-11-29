from modelo_usuario import Usuario
from controlador_usuario import ControladorUsuario

class ControladorLogin:
    def __init__(self) -> None:
        self.controlador_usuario = ControladorUsuario("usuarios")
        self.controlador_usuario.conectar_banco()
    
    def verificar_senha(self, nome, salted_hash):
        usuario = self.controlador_usuario.buscar_usuario_por_nome(nome)
        if isinstance(usuario, str):
            return False
        if usuario.salted_hash == salted_hash:
            return True
