class Usuario:
    def __init__(self, id: int, nome: str, email: str, password_hash: str) -> None:
        self.id: int = id
        self.nome: str = nome
        self.email: str = email
        self.password_hash: str = password_hash