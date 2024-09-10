from abc import ABC, abstractmethod
# 1 - Crie uma classe chamada Veiculo com um método abstrato chamado ligar.
class Veiculo(ABC):
# 2 - No mesmo arquivo, crie um construtor para a classe Veiculo que aceita os parâmetros marca e modelo.
  def __init__(self, marca, modelo):
    self._marca = marca
    self._modelo = modelo

  def __str__(self):
    return f'{self._marca}'

  @abstractmethod
  def ligar(self):
    pass