class Bingo:
    def __init__(self):
        self.__numBo = 0
        self.__bolas = 0
    def set_numBo(self, q):
        if q > 0: return self.__numBo == q
        else: raise ValueError("Quantia de bolas inválida")
    def get_numBo(self):
        return self.__numBo
    


class BingoUI:
    @staticmethod
    def menu():
        op = int(input('Escolha uma opção: 1-Iniciar um novo jogo 2 -Sortear um número 3-verificar números 4-Sair '))
        return op
    @staticmethod
    def main():
        op = 0
        while op != 4:
            op = BingoUI.menu()
            if op == 1: #BingoUI.iniciar()
            elif op == 2: Bin
    