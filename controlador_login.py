class ControladorLogin:
    def __init__(self) -> None:
        pass

    def cadastrar(self, nome, senha):
        file = open("teste.txt", "a")
        file.write(str(nome + ' ' + senha))
        file.write('\n')
        file.close()
    
    def verificar_senha(self, nome, senha):
        with open("teste.txt", "r") as file:
            texto = file.readlines()
            for linha in texto:
                if str(nome + ' ' + senha) in linha:
                    return True
            return False