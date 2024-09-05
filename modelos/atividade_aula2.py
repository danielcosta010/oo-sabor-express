# Atividade anterior
class Musica:
  musicas = []
  def __init__(self, nome, artista, duracao):
    self.nome = nome
    self.artista = artista
    self.duracao = duracao
    Musica.musicas.append(self)

  def __str__(self):
    return f'{self.nome} | {self.artista}'
  
  def lista_musicas():
    for musica in Musica.musicas:
      print(f'{musica.nome} | {musica.artista} | {musica.duracao}')

musica1 = Musica('Papapa', 'Pato', 355)

Musica.lista_musicas()

# Exercícios praticos
def cria_linha(atividade):
  linha = '=' * (len(atividade))
  print(linha)

def mostra_linha(atividade):
  cria_linha(atividade)
  print(atividade)
  cria_linha(atividade)

atividade_1 = '1 - Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.'
mostra_linha(atividade_1)
class Carro:
  carros = []
  def __init__(self, modelo, cor, ano):
    self.modelo = modelo
    self.cor = cor
    self.ano = ano
    Carro.carros.append(self)

  def __str__(self):
    return f'{self.modelo} | {self.cor} | {self.ano}'
  
  def cadastrar_carros():
    modelo = input('Digite o modelo do carro: ')
    cor = input('Digite a cor do carro: ')
    ano = int(input('Digite o ano do carro: '))
    carro = Carro(modelo, cor, ano)
    print(f'O carro {carro.modelo} foi cadastrado.')


  def listar_carros():
    for carro in Carro.carros:
      print(f'Resposta 1: {carro.modelo} | {carro.cor} | {carro.ano}')

carro_onix = Carro('Onix', 'Azul', 2014)
carro_onix = Carro('Gol', 'preto', 2010)

Carro.listar_carros()
print()

atividade_2 = '2, 3, 4-Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores a eles'
mostra_linha(atividade_2)
class Restaurante:
  restaurantes = []
  def __init__(self, nome, categoria, ativo, capacidade, endereco):
    self.nome = nome
    self.categoria = categoria
    self.ativo = ativo
    self.capacidade = capacidade
    self.endereco = endereco
    Restaurante.restaurantes.append(self)

  def __str__(self):
    return f'{self.nome} | {self.categoria} | {self.ativo} | {self.capacidade} | {self.endereco}'
  
  def listar_restaurantes():
    for restaurante in Restaurante.restaurantes:
      print(f'Resposta 2: {restaurante.nome} | {restaurante.categoria} | {restaurante.ativo} | {restaurante.capacidade} | {restaurante.endereco}')

restaurante_paris = Restaurante('Ratatoulli', 'Francesa', False, 120, 'Rua: Paris')
Restaurante.listar_restaurantes()
print()

atividade_5 = 'Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.'
mostra_linha(atividade_5)
class Cliente:
  clientes = []
  def __init__(self, nome, conta, email, telefone):
    self.nome = nome
    self.conta = conta
    self.email = email
    self.telefone = telefone
    Cliente.clientes.append(self)

  def listar_clientes():
    for cliente in Cliente.clientes:
      print(f'Resposta 5: {cliente.nome} | {cliente.conta} | {cliente.email} | {cliente.telefone}')

cliente_1 = Cliente('Daniel', 'Corrente', 'dan@dan.com', 12344321)
cliente_2 = Cliente('Polliana', 'Corrente', 'pol@pol.com', 43322222)
cliente_3 = Cliente('Isabella', 'Poupança', 'bela@bela.com', 1212232)
Cliente.listar_clientes()