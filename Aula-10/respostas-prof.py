import random

class Bingo:
    def __init__(self, num_bolas):
        self.__num_bolas = num_bolas
        if num_bolas <  5: raise ValueError("Número mínimo de bolas é 5")
        self.__bolas = []
    def sortear(self):
        x = random.randint(1, self.__bolas)
        while x in self.__bolas:
            x = random.randint(1, self.__bolas)
        self.__bolas.append(x)
    def sorteados(self):
        return sorted(self.__bolas)

jogo = Bingo(10)
print(jogo.sortear())