class Viagem:
    def __init__(self):
        self.__dst = ''
        self.__km = 0
        self.__l = 0.0
    def set_dst(self, d):
        if d != "": self.__dst = d
        else: raise ValueError('Destino não pode ser vazio.')
    def set_km(self,k):
        if k > 0: self.__km = k
        else: raise ValueError('A distância deve ser maior ou igual a zero.')
    def set_l(self, lt):
        if lt > 0: self.__l = lt
        else: raise ValueError('Quantidade litros inválida (não pode ser zero).')
    def get_dst(self):
        return self.__dst
    def get_km(self):
        return self.__km
    def get_l(self):
        return self.__l
    def consumo(self):
        return self.__km / self.__l
    

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

        print(f'A quantidade de litros que foi consumida foi: {x.consumo():.2f}')

ViagemUI.main()

        


          