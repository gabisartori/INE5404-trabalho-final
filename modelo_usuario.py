import random

class Usuario:
    def __init__(self, id: int, nome: str, password_hash: str) -> None:
        self.id: int = id
        self.nome: str = nome
        self.salt: str = str(random.randint(1, 1_000_000))
        self.password_hash: str = password_hash
