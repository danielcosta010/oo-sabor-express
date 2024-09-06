from modelos.restaurante import Restaurante

restaurante_boizao = Restaurante('bOizão', 'Currascaria')
restaurante_forno = Restaurante('Forno de bArRo', 'Italiana')
retaurante_beef = Restaurante('Baby-beef', 'mineira')

restaurante_boizao.alternar_status()
restaurante_boizao.receber_avaliacao('Daniel', 9)
restaurante_boizao.receber_avaliacao('Isabella', 7)
restaurante_boizao.receber_avaliacao('Polliana', 10)

def main():
  Restaurante.listar_restaurantes()

if __name__ == '__main__':
  main()