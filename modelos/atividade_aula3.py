def linha(atividade):
  linha = '=' * (len(atividade))
  linha = linha[:153]
  print(linha)

def mostra_linha(atividade):
  linha(atividade)
  print(atividade)
  linha(atividade)

atividade = 'Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. Adicione um método especial __str__ para imprimir uma representação em string da pessoa. Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.'
print(atividade)
class Pessoa:
  pessoas =[]
  def __init__(self, nome='', profissao='', idade=0):
    self.nome = nome
    self.profissao = profissao
    self.idade = idade
    Pessoa.pessoas.append(self)

  def __str__(self):
    return f'{self.nome} é um(a) {self.profissao} com {self.idade} anos'
  
  @classmethod
  def listar_pessoa(cls):
    for pessoa in cls.pessoas:
      print(f'{pessoa.nome} | {pessoa.profissao} | {pessoa.idade} anos')
  
  
  def aniversario(self):
    self.idade += 1

  @property
  def saudacao(self):
    if self.profissao:
      print(f'Olá sou {self.nome} minha profissão é {self.profissao}')
    else:
      print(f'Olá sou {self.nome}')
  
pessoa_1 = Pessoa(nome='Daniel', profissao='Programador', idade=41)
pessoa_2 = Pessoa(nome='Isabella', idade=10)
pessoa_3 = Pessoa(nome='Polliana', profissao='Fisioterapeuta', idade=41)

Pessoa.listar_pessoa()
pessoa_1.aniversario()
pessoa_1.aniversario()
pessoa_2.aniversario()
pessoa_3.aniversario()
pessoa_3.aniversario()
pessoa_3.aniversario()
Pessoa.listar_pessoa()
pessoa_1.saudacao
pessoa_2.saudacao
pessoa_3.saudacao

atividade_1 = '1-Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.'
mostra_linha(atividade_1)
class ContaBancaria:
  clientes = []
  def __init__(self, titular='', saldo=0, ativo=False):
    self.titular = titular
    self.saldo = saldo
    self._ativo = ativo
    ContaBancaria.clientes.append(self)
# atividade 2
  def __str__(self):
    return f'{self.titular} {self.saldo} {self.ativo}'
  
# atividade 3 e 4.
  @classmethod
  def lista_clientes(cls):
    for cliente in cls.clientes:
      print(f'{cliente.titular} tem um saldo de {cliente.saldo} e sua conta está {cliente.ativo}')
                                                     
  def alterna_status_da_conta(self):
    self._ativo = not self._ativo

  @property
  def ativo(self):
    return '✅' if self._ativo else '❌'
  
cliente_1 = ContaBancaria(titular='Daniel', saldo='5.000.000,00')
cliente_2 = ContaBancaria(titular='Polliana', saldo='15.000.000,00')

cliente_1.alterna_status_da_conta()
cliente_2.alterna_status_da_conta()

ContaBancaria.lista_clientes()


atividade_6 = '6 e 7 - Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor. Crie um método de classe para a conta ClienteBanco.'
mostra_linha(atividade_6)
class ClienteBanco:
  clientes = []
  def __init__(self, nome='', tipo_de_conta='', cpf=0, telefone=0, endereco=''):
    self.nome = nome
    self.tipo_de_conta = tipo_de_conta
    self.cpf = cpf
    self.telefone = telefone
    self.endereco = endereco
    ClienteBanco.clientes.append(self)
  
  # def __str__(self):
  #   return f'{self.nome} {self.idade} {self.cpf} {self.telefone} {self.endereco}'

  @classmethod
  def lista_clientes(cls):
    for cliente in cls.clientes:
      print(f'{cliente.nome} possui conta {cliente.tipo_de_conta}, seu telefone é {cliente.telefone}, cpf: {cliente.cpf} e mora em {cliente.endereco}')
  


cliente_1 = ClienteBanco(nome='Daniel', tipo_de_conta='Corrente', cpf=29876543210, telefone=234321234, endereco='Rua: Leste')
cliente_2 = ClienteBanco(nome='Polliana', tipo_de_conta='Corrente', cpf=29876543210, telefone=234321234, endereco='Rua: Leste')
cliente_2 = ClienteBanco(nome='Isabella', tipo_de_conta='Poupança', cpf=29876543210, telefone=234321234, endereco='Rua: Leste')

ClienteBanco.lista_clientes()