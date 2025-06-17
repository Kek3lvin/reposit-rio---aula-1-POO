class Viagem:
    def __init__(self):
        self.__dst = ''
        self.__km = 0
        self.__l = 0.0
    # ____ENCAPSULAMENTO____#
    def set_dst(self, d):
        if d != "": self.__dst = d
        else: raise ValueError('Destino não pode ser vazio.')
    def set_km(self,k):
        if k > 0: self.__km = k
        else: raise ValueError('A distância deve ser maior que zero.')
    def set_l(self, lt):
        if lt > 0: self.__l = lt
        else: raise ValueError('Quantidade litros inválida (não pode ser zero).')
    def get_dst(self):
        return self.__dst
    def get_km(self):
        return self.__km
    def get_l(self):
        return self.__l
    # _____MÉTODO_____#
    def consumo(self):
        return self.__km / self.__l
    def __str__(self):
        return f' Destino: {self.__dst}, Quilômetros: {self.__km}, Litros: {self.__l}. Quantidade de litros consumida: {self.consumo():.2f}'

class ViagemUI: # Interface do usuário
    @staticmethod
    def menu():
        op = int(input('Escolha uma opção: 1-Calcular 2-Fim'))
        return op
    @staticmethod
    def main(): # LOOP 
        op = 0
        while op != 2:
         op = ViagemUI.menu()
         if op == 1: ViagemUI.calcular()
    @staticmethod
    def calcular(): # Usuário atribui valores aos paramêtros
        x = Viagem()
        x.set_dst(input('Informe o seu destino:'))
        x.set_km(float(input('Informe a distância percorrida:')))
        x.set_l(float(input('Informe a quantida de litros:')))
        print(x)
                
ViagemUI.main()

        


          