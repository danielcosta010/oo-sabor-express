from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante_boizao = Restaurante('bOizão', 'Currascaria')
restaurante_forno = Restaurante('Forno de bArRo', 'Italiana')
retaurante_beef = Restaurante('Baby-beef', 'mineira')

restaurante_boizao.alternar_status()
bebida_suco = Bebida('Suco de Laranja', 5.00, 'Grande')
prato_paozinho = Prato('Paozinho', 2.00, 'O melho pão frances')
restaurante_boizao.adiciona_no_cardapio(bebida_suco)
restaurante_boizao.adiciona_no_cardapio(prato_paozinho)

def main():
  restaurante_boizao.exibir_cardapio

if __name__ == '__main__':
  main()