from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.sobremesa import Sobremesa

restaurante_boizao = Restaurante('bOizão', 'Currascaria')
restaurante_forno = Restaurante('Forno de bArRo', 'Italiana')
retaurante_beef = Restaurante('Baby-beef', 'mineira')

restaurante_boizao.alternar_status()
bebida_suco = Bebida('Suco de Laranja', 5.00, 'Grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Paozinho', 2.00, 'O melho pão frances')
prato_paozinho.aplicar_desconto()
sobremesa_pudin = Sobremesa('Pudim', 8.00, 'De leite', 'Medio', 'Delicioso Pudim de leite' )
restaurante_boizao.adiciona_no_cardapio(bebida_suco)
restaurante_boizao.adiciona_no_cardapio(prato_paozinho)
restaurante_boizao.adiciona_no_cardapio(sobremesa_pudin)

def main():
  restaurante_boizao.exibir_cardapio

if __name__ == '__main__':
  main()