class Restaurante:
  restaurantes = []

  def __init__(self, nome, categoria):
    self.nome = nome
    self.categoria = categoria
    self.ativo = False
    Restaurante.restaurantes.append(self)

  def __str__(self):
    return f'{self.nome} | {self.categoria}'
  
  def listar_restaurantes():
    for restaurante in Restaurante.restaurantes:
      print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')


restaurante_boizao = Restaurante('Boizão', 'Churrascaria')

restaurante_forno = Restaurante('Frono de Barro', 'Italiana')

Restaurante.listar_restaurantes()

