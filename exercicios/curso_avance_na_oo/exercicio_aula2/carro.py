# 3 - Crie uma nova classe chamada Carro que herda da classe Veiculo.

from veiculo import Veiculo

class Carro(Veiculo):
# 4 - No construtor da classe Carro, utilize o método super() para chamar o construtor da classe pai e atribua o atributo específico cor à classe filha.
  def __init__(self, marca, modelo, cor):
    super().__init__(marca, modelo)
    self.cor = cor

  def __str__(self):
    return f'{self._marca} | {self._modelo} | {self.cor}'
  
  def ligar(self):
    return f'E está ligado'
