class Usuario:
    def __init__(self, id, nome, email, password_hash) -> None:
        self.id: int = id
        self.nome: str = nome
        self.email: str = email
        self.password_hash: str = password_hash