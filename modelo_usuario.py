class Usuario:
    def __init__(self, id: int, nome: str, salt: str, password_hash: str) -> None:
        self.id: int = id
        self.nome: str = nome
        self.salt: str = salt
        self.salted_hash: str = password_hash