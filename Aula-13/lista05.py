from datetime import datetime

# 1 - Um paciente
class Paciente:
    def __init__(self, n, c, t, ns):
        self.__n = n
        self.__c = c
        self.__t = t
        self.__ns =  datetime.strptime(ns, '%d/%m/%Y')

    def get_n(self): return self.__n
    def get_c(self): return self.__c
    def get_t(self): return self.__t
    def get_ns(self): return self.__ns
    def idade(self):
        atual = datetime.today()
        dias_v = atual - self.__ns
        print(dias_v.days // 365, 'anos', end = ' e ')
        print(dias_v.days % 365 // 30, 'meses')
    
    def __str__(self):
         return f"Nome: {self.__n} - CPF: {self.__c} - Telefone: {self.__t} - Data de nascimento: {self.__ns} "
    
class PacienteUI:
    __cadastrados = []
    @classmethod
    def menu(cls):
        op = int(input('Escolha uma opção: 1-Cadastrar paciente, 2-Listar, 3-Idade, 4-Atualizar, 5-sair: '))
        return op
    @classmethod
    def main(cls):
        op = 0
        while op != 5:
            op = PacienteUI.menu()
            if op == 1: PacienteUI.cadastrar()
            if op == 2: PacienteUI.listar()
            if op == 3: PacienteUI.idade()
            if op == 4: PacienteUI.atualizar()
    @classmethod
    def cadastrar(cls):
        nome = input('Informe o nome do paciente: ')
        cpf = (input('Informe o CPF do paciente:  '))
        fone = (input('Informe o telefone do paciente:  '))
        dn = (input('Informe a data de nascimento do paciente:  '))
        dados = Paciente(nome, cpf, fone, dn)
        cls.__cadastrados.append(dados)
    @classmethod
    def listar(cls):
        for p in cls.__cadastrados:
            print(p)
        if len(cls.__cadastrados) == 0:
            print('Nenhum paciente foi cadastrado ainda.')
    @classmethod
    def idade(cls):
        cpf = input("Informe o CPF do paciente: ")
        for p in cls.__cadastrados:
            if p.get_c() == cpf:
                print(f"A idade de {p.get_n()} é: ")  
                (p.idade())
            else:
                print("Paciente não encontrado.")
    @classmethod
    def atualizar(cls):
        cpf = input('Informe o CPF do paciente para editar os dados: ')
        for c in cls.__cadastrados:
            if c.get_c() == cpf:
                 n_nome = input('Informe o novo nome do paciente: ')
                 n_cpf = (input('Informe o novo CPF do paciente:  '))
                 n_fone = (input('Informe o novo telefone do paciente:  '))
                 n_dn = (input('Informe a nova data de nascimento do paciente:  '))
                 n_dados = Paciente(n_nome, n_cpf, n_fone, n_dn)
                 cls.__cadastrados.remove(c)
                 cls.__cadastrados.append(n_dados)
                 print('Dados atualizados')

PacienteUI.main()