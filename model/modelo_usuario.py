class Usuario:
    def __init__(self, id: int, nome: str, sal: str, hash_salteada: str) -> None:
        self.__id: int = id
        self.__nome: str = nome
        self.__sal: str = sal
        self.__hash_salteada: str = hash_salteada

    def get_id(self) -> int:
        return self.__id
    
    def get_nome(self) -> str:
        return self.__nome
    
    def set_nome(self, nome: str) -> None:
        self.__nome = nome

    def get_sal(self) -> str:
        return self.__sal
    
    def set_sal(self, sal: str) -> None:
        self.__sal = sal

    def get_hash_salteada(self) -> str:
        return self.__hash_salteada
    
    def set_hash_salteada(self, hash_salteada: str) -> None:
        self.__hash_salteada = hash_salteada
