

class UI: # UI = User Interface: print e input
    @staticmethod
    def menu():
        op = int(input("Informe uma opção: 1-Conta d'água, 2-Triângulo, 9-Fim: "))
        return op
    @staticmethod
    def main():
        op = 0
        while op != 9:
           # op = self.menu()
           op = UI.menu()
           if op == 1: UI.agua()
           if op == 2: UI.triangulo()
    @staticmethod
    def agua():
        x = Agua() # x é um objeto da classe Água

        # x.mes = int(input("Informe o mês da conta: "))
        x.set_mes(int(input("Informe o mês da conta: ")))

        # x.ano = int(input("informe o ano: "))
        x.set_ano(int(input("informe o ano: ")))

        # x.consumo = int(input("informe o consumo em m3: "))
        x.set_consumo(int(input("informe o consumo em m3: ")))
        
        #print(x.__mes, x.__ano, x.__consumo)
        # __mes, __ano e __consumo não são visíveis

        #print(f"O valor da conta de água do mês {x.mes} do ano {x.ano} é {x.valor()}")
        print(f"O valor da conta de água do mês {x.get_mes()} do ano {x.get_ano()} é {x.valor()}")
    @staticmethod
    def triangulo():
        x = Triangulo() # x é um objeto da classe Triangulo
        x.b = int(input("Informe o valor da base: "))
        x.h = int(input("Informe o valor da altura: "))
        print(f"O triângulo de base {x.b} e altura {x.h} tem área {x.calc_area()}")

#x = UI()
#x.main()
UI.main()


