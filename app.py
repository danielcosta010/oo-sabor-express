from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante_boizao = Restaurante('bOizão', 'Currascaria')
restaurante_forno = Restaurante('Forno de bArRo', 'Italiana')
retaurante_beef = Restaurante('Baby-beef', 'mineira')

restaurante_boizao.alternar_status()
bebida_suco = Bebida('Suco de Laranja', 5.00, 'Grande')
prato_paozinho = Prato('Paozinho', 2.00, 'O melho pão frances')

def main():
  print(bebida_suco)
  print(prato_paozinho)

if __name__ == '__main__':
  main()