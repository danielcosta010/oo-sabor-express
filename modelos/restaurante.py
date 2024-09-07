from modelos.avaliacao import Avaliacao
import os

class Restaurante:
  '''Cria um novo restaurante'''
  restaurantes = []

  def __init__(self, nome, categoria):
    '''Inicializa uma instância do restaurante
    
    Parametros:
      nome (str): Nome do restaurante
      categoria (str): Categoria do restaurante
    
    '''
    self._nome = nome.title()
    self._categoria = categoria.upper()
    self._ativo = False
    self._avaliacao = []
    Restaurante.restaurantes.append(self)

  def __str__(self):
    '''Retorna uma representação em string dos dados do restaurante'''
    return f'{self._nome} | {self._categoria}'
  
  @classmethod
  def listar_restaurantes(cls):
    ''''Retorna uma lista formatada de restaurantes'''
    print()
    print(f"{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliações'.ljust(25)} | {'Status'}")
    print('-' * 100)
    for restaurante in cls.restaurantes:
      print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')
    print()

  @property
  def ativo(self):
    '''Retorna um símbolo baseado no status do restaurante'''
    return '❎' if self._ativo else '🟩'
  
  def alternar_status(self):
    '''Alterna o stados do restaurante'''
    self._ativo = not self._ativo

  def receber_avaliacao(self, cliente, nota):
    ''''Recebe um avaliação do cliente entre 1 e 5
    Parametros:
    - cliente(str) = nome do cliente
    - nota(int) = nota do cliente entre 1 e 5
    '''
    if 0 < nota <= 5:
      avaliacao = Avaliacao(cliente, nota)
      self._avaliacao.append(avaliacao)
    else: 
      print('Nota deve ser entre 0 e 5, será desconsiderada.')
      input('Pressione Enter para continuar...')

  @property
  def media_avaliacoes(self):
    ''''Calcula a média das avaliações do restaurante'''
    if not self._avaliacao:
      return 5
    soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
    quantidade_de_notas = len(self._avaliacao)
    media = round(soma_das_notas / quantidade_de_notas, 1)
    return media



