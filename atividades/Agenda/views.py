from models.cliente import Cliente, ClienteDAO
from models.servicos import Servico, ServicoDAO
from models.horario import Horario, HorarioDAO

class View: 
    # 1° view Cliente
    def cliente_listar():
        return ClienteDAO.listar()
    def cliente_inserir(nome, email, fone):
        cliente = Cliente(0, nome, email, fone)
        ClienteDAO.inserir(cliente)
    def cliente_atualizar(id, nome, email, fone):
        cliente = Cliente(id, nome, email, fone)
        ClienteDAO.atualizar(cliente)
    def cliente_excluir(id):
        cliente = Cliente(id, "", "", "")
        ClienteDAO.excluir(cliente)
    
    #2° view Servico
    def servico_listar():
        return ServicoDAO.listar()
    def servico_inserir(desc, valor):
        servico = Servico(0, desc, valor)
        ServicoDAO.inserir(servico)
    def servico_atualizar(id, desc, valor):
        servico = Servico(id, desc, valor)
        ServicoDAO.atualizar(servico)
    def servico_excluir(id):
        servico = Servico(id, "", "")
        ServicoDAO.excluir(servico)
 
    #3° view Horario
    def horario_inserir(data, confirmado, id_cliente, id_servico):
      c = Horario(0, data)
      c.set_confirmado(confirmado)
      c.set_id_cliente(id_cliente)
      c.set_id_servico(id_servico)
      HorarioDAO.inserir(c)
    def horario_listar():
      return HorarioDAO.listar()  
    def horario_atualizar(data, confirmado, id_cliente, id_servico):
      c = Horario(0, data)
      c.set_confirmado(confirmado)
      c.set_id_cliente(id_cliente)
      c.set_id_servico(id_servico)
      HorarioDAO.inserir(c)
    def horario_excluir():
      c = HorarioDAO.listar(id, None)  
      HorarioDAO.excluir(c)
    
