from datetime import datetime

class Contatos:
    def __init__(self, id, n, e, t, ns):
        self.__id = id
        self.__nome = n
        self.__email = e
        self.__telefone =  t
        self.__nascimento = datetime.strptime(ns.strip(), '%d/%m/%Y')
    
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__telefone
    def get_nas(self): return self.__nascimento

    def __str__(self):
       return  f'id: {self.__id}, Nome: {self.__nome}, Email: {self.__email}, Telefone: {self.__telefone}, Data de nascimento: {self.__nascimento}'
    
class ContatoUI:
    __contatos = []
    @classmethod    
    def main(cls):
        op = 0
        while op != 7:
            op = ContatoUI.menu()
            if op == 1: ContatoUI.inserir()
            if op == 2: ContatoUI.listar()
            if op == 3: ContatoUI.atualizar()
            if op == 4: ContatoUI.excluir()
            if op == 5: ContatoUI.pesquisar()
            if op == 6: ContatoUI.aniversariantes()
            if op == 7: print('Saindo')
            
    @classmethod    
    def menu(cls):
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 5-Pesquisar, 6-Ver os aniversariantes do mês, 7-Sair")
        return int(input("Escolha uma opção: "))
    
    @classmethod    
    def inserir(cls):
        id = int(input("Informe o id do contato: "))
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o fone: ")
        nascimento = input('Informe a data de nascimento desse contato: ')
        c = Contatos(id, nome, email, fone, nascimento)
        cls.__contatos.append(c)
    @classmethod    
    def listar(cls):
        if len(cls.__contatos) == 0: print('Nenhum contato cadastrado')
        for c in cls.__contatos:
            print(c)
    @classmethod

    def atualizar(cls):
       id = int(input("Informe o id do contato que você quer atualizar:"))
       for i in cls.__contatos:
          if i.get_id() == id:
            nome = input("Informe o novo nome: ")
            email = input("Informe o novo email: ")
            fone = input("Informe o novo fone: ")
            nascimento = input('Informe a nova data de nascimento:')
            y = Contatos(id, nome, email, fone, nascimento)
            cls.__contatos.remove(i)
            cls.__contatos.append(y)
            print('Dados atualizados!')
          else:
            print('Id inexistente.')

    @classmethod    
    def excluir(cls):
        nome = input('Informe o nome do contato que deseja excluir: ')
        for n in cls.__contatos:
            if n.get_nome() == nome:
                cls.__contatos.remove(n)
                print('Contato removido!')

    @classmethod    
    def pesquisar(cls):
        nome = input("Informe a inicial do nome que deseja pesquisar: ")
        for c in cls.__contatos:
            if c.get_nome().startswith(nome): print(c)
    
    @classmethod
    def aniversariantes(cls):
     mes = int(input("Informe o número do mês (1-12): ").strip())
     encontrados = False
     for c in cls.__contatos:
        if c.get_nas().month == mes:
            if not encontrados:
                print(f"O(s) aniversariante(s) do mês {mes} é(são):")
            print(c.get_nome())
            encontrados = True
     if not encontrados:
        print("Nenhum aniversariante encontrado nesse mês.")

ContatoUI.main()
