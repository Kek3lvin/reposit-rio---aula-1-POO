from datetime import datetime

# 1 - Um paciente
class Paciente:
    def __init__(self, n, c, t, ns):
        self.__n = n
        self.__c = c
        self.__t = t
        self.__ns =  ns

    def get_n(self): return self.__n
    def get_c(self): return self.__c
    def get_t(self): return self.__t
    def get_ns(self): return self.__ns
    def idade(self):
        atual = datetime.now()
        d = input('Informe sua data de nascimento: ')
        self.__ns = datetime.strptime(d, '%d/%m/%y')
        return self.__ns
    def __str__(self):
         return f"Nome: {self.__n} - CPF: {self.__c} - Telefone: {self.__t} "
class PacienteUI:
    __p_cadastrados = []
    @classmethod
    def menu():
        op = int(input('Escolha uma opção: 1-Cadastrar paciente, 2-Listar, 3-Idade, 4-Atualizar, 5-sair'))
        return op
    def main():
        op = 0
        while op != 5:
            if op == 1: PacienteUI.cadastro()
            if op == 2: PacienteUI.listar()
            if op == 3: PacienteUI.Idade()
            if op == 4: PacienteUI.atualizar()
            else: print('Saindo...')