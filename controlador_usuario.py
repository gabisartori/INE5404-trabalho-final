from modelo_usuario import Usuario
import json

class ControladorUsuario:
    def __init__(self, db="usuarios") -> None:
        self.db = db
        self.usuarios: list = None

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

    def atualizar_usuario(self, id: int, novo_nome: str, nova_senha: str) -> Usuario | str:
        with open(f"{self.db}.json") as file:
            usuarios = json.load(file)
        
        usuario = [usr for usr in usuarios if usr["id"] == id][0]
        if novo_nome: usuario["nome"] = novo_nome
        if nova_senha: 
            usuario["salted_hash"] = nova_senha

        with open(f"{self.db}.json", 'w') as file:
            json.dump(usuarios, file)
        
        return usuario

    def remover_usuario(self, id_nome: int | str) -> Usuario | str:
        usuario = [usr for usr in self.usuarios if usr["nome"] == id_nome or usr["id"] == id_nome][0]
        self.usuarios.remove(usuario)
        with open(f"{self.db}.json", 'w') as file:
            json.dump(self.usuarios, file)
        return usuario
