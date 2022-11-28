import random
import hashlib

class Usuario:
    def __init__(self, id: int, nome: str, password: str) -> None:
        self.id: int = id
        self.nome: str = nome
        self.salt: str = str(random.randint(1, 1_000_000))
        self.salted_hash: str = hashlib.sha256((password + self.salt).encode()).hexdigest()
