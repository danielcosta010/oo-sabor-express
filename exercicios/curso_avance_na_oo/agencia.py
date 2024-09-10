from banco import Banco

class Agencia(Banco):
  def __init__(self, nome, endereco, numero):
    super().__init__(nome, endereco)
    self.numero = numero

  def __str__(self):
    return f'Agência: {self.nome}, Endereço: {self.endereco}, Número: {self.numero}'
  

cliente_1 = Agencia('Daniel', 'Rua: dos Lucros', 1212343221)
print(cliente_1)