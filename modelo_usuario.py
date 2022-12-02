class Usuario:
    def __init__(self, id: int, nome: str, salt: str, password_hash: str) -> None:
        self.__id: int = id
        self.__nome: str = nome
        self.__salt: str = salt
        self.__salted_hash: str = password_hash

    def get_id(self) -> int:
        return self.__id
    
    def get_nome(self) -> str:
        return self.__nome
    
    def set_nome(self, nome: str) -> None:
        self.__nome = nome

    def get_salt(self) -> str:
        return self.__salt
    
    def set_salt(self, salt: str) -> None:
        self.__salt = salt

    def get_salted_hash(self) -> str:
        return self.__salted_hash
    
    def set_salted_hash(self, salted_hash: str) -> None:
        self.__salted_hash = salted_hash

