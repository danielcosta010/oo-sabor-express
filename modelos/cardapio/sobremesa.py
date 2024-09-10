from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
  def __init__(self, nome, preco, tipo, peso, lista):
    super().__init__(nome, preco)
    self.tipo = tipo
    self.peso = peso
    self.lista = lista

  def __str__(self):
    return f'{self._nome} | {self._preco} | {self.tipo} | {self.peso} | {self.lista}'
  
  def aplicar_desconto(self):
    pass