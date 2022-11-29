from modelo_usuario import Usuario
import json

class ControladorUsuario:
    def __init__(self, db) -> None:
        self.db = db
        self.usuarios = None

    def conectar_banco(self) -> None:
        """Atualiza a lista de usuários se baseando no banco de dados"""
        with open(f"{self.db}.json") as file:
            self.usuarios = json.load(file)

    def buscar_usuario_por_id(self, id: int) -> Usuario:
        for usuario in self.usuarios:
            if usuario['id'] == id:
                return Usuario(usuario['id'], usuario['nome'], usuario['salt'], usuario['salted_hash'])
    
    def buscar_usuario_por_nome(self, nome: str) -> Usuario | str:
        for usuario in self.usuarios:
            if usuario['nome'] == nome:
                return Usuario(usuario['id'], usuario['nome'], usuario['salt'], usuario['salted_hash'])
        return "Usuário não encontrado"

    # Fazer no controlador de Cadastro
    def cadastrar_usuario(self, usuario: Usuario) -> Usuario | str:
        pass

    def atualizar_usuario(self, id: int, usuario: Usuario) -> Usuario | str:
        pass

    def remover_usuario(self, id: int) -> Usuario | str:
        for usuario in self.usuarios:
            if usuario['id'] == id:
                self.usuarios.remove(usuario)
                with open(f"{self.db}.json", 'w') as file:
                    json.dump(self.usuarios, file)
                return usuario
