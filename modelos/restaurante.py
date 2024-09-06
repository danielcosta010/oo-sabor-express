class Restaurante:
  restaurantes = []

  def __init__(self, nome, categoria):
    self._nome = nome.title()
    self._categoria = categoria.upper()
    self._ativo = False
    Restaurante.restaurantes.append(self)

  def __str__(self):
    return f'{self._nome} | {self._categoria}'
  
  
  @classmethod
  def listar_restaurantes(cls):
    print()
    print(f"{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}")
    print('-' * 75)
    for restaurante in cls.restaurantes:
      print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')
    print()

  @property
  def ativo(self):
    return '❎' if self._ativo else '🟩'
  
  def alternar_status(self):
    self._ativo = not self._ativo


restaurante_boizao = Restaurante('Boizão', 'Churrasca')
restaurante_boizao.alternar_status()
restaurante_forno = Restaurante('forno de barro', 'Italiana')


Restaurante.listar_restaurantes()

