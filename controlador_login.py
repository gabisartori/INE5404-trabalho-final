from controlador_usuario import ControladorUsuario


class ControladorLogin(ControladorUsuario):
    def __init__(self, db="usuarios") -> None:
        super().__init__(db)
        self.conectar_banco()
    
    def verificar_senha(self, nome: str, salted_hash: str) -> bool:
        """Checa se a hash calculada (passada nos parâmetros) bate com a hash salva no banco de dados"""
        usuario = self.buscar_usuario_por_nome(nome)
        if isinstance(usuario, str):
            return False
        return usuario.get_salted_hash() == salted_hash
