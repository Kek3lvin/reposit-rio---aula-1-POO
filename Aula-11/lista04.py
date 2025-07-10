class Contato:
    def __init__(self, i, n, e, f):
        self.__id = i
        self.__nome = n
        self.__email = e
        self.__fone = f
    def get_nome(self):
        return self.__nome 
    def get_id(self):
        return self.__id
    def get_email(self):
        return self.__email
    def get_fone(self):
        return self.__fone
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"

class ContatoUI:
    __contatos = []
    @classmethod    
    def main(cls):
        op = 0
        while op != 6:
            op = ContatoUI.menu()
            if op == 1: ContatoUI.inserir()
            if op == 2: ContatoUI.listar()
            if op == 3: ContatoUI.atualizar()
            if op == 4: ContatoUI.excluir()
            if op == 5: ContatoUI.pesquisar()
            
    @classmethod    
    def menu(cls):
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 5-Pesquisar, 6-Fim")
        return int(input("Escolha uma opção: "))
    
    @classmethod    
    def inserir(cls):
        id = int(input("Informe o id do contato: "))
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o fone: ")
        c = Contato(id, nome, email, fone)
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
            y = Contato(id, nome, email, fone)
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

ContatoUI.main()
