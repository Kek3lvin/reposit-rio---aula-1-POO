from models.cliente import Cliente, ClienteDAO
from models.servicos import Servico, ServicoDAO
from models.horario import Horario, HorarioDAO
from models.profissional import Profissional, ProfissionalDAO

class View: 
    # 1° view Cliente
    def cliente_listar():
        return ClienteDAO.listar()
    def cliente_listar_id(id):
        cliente = ClienteDAO.listar_id(id)
        return cliente
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
    def servico_listar_id(id):
        servico = ServicoDAO.listar_id(id)
        return servico
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
    def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
      c = Horario(0, data)
      c.set_confirmado(confirmado)
      c.set_id_cliente(id_cliente)
      c.set_id_servico(id_servico)
      c.set_id_profissional(id_profissional)
      HorarioDAO.inserir(c)

    def horario_listar():
      return HorarioDAO.listar()  
    
    def horario_atualizar(data, confirmado, id_cliente, id_servico, id_profissional):
      c = Horario(id, data)
      c.set_confirmado(confirmado)
      c.set_id_cliente(id_cliente)
      c.set_id_servico(id_servico)
      c.set_id_profissional(id_profissional)
      HorarioDAO.inserir(c)
      
    def horario_excluir(id):
      c = Horario(id, None)  
      HorarioDAO.excluir(c)
    
    #4° View Profissional
    def profissional_listar():
        return ProfissionalDAO.listar()
    def profissional_listar_id(id):
        profissional = ProfissionalDAO.listar_id(id)
        return profissional
    def profissional_inserir(nome, especialidade, conselho):
        profissional = Profissional(0, nome, especialidade, conselho)
        ProfissionalDAO.inserir(profissional)
    def profissional_atualizar(id, nome, especialidade, conselho):
        profissional = Profissional(id, nome, especialidade, conselho)
        ProfissionalDAO.atualizar(profissional)
    def profissional_excluir(id):
        profissional = Profissional(id, "", "", "")
        ProfissionalDAO.excluir(profissional)