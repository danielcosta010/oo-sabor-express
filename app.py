from modelos.restaurante import Restaurante


restaurante_boizao = Restaurante('bOizão', 'Currascaria')
restaurante_forno = Restaurante('Forno de bArRo', 'Italiana')
retaurante_beef = Restaurante('Baby-beef', 'mineira')

restaurante_boizao.alternar_status()
restaurante_boizao.receber_avaliacao('Daniel', 5)
restaurante_boizao.receber_avaliacao('Daniel', 6)
restaurante_boizao.receber_avaliacao('Isabella', 3)
restaurante_boizao.receber_avaliacao('Polliana', 4)

def main():
  Restaurante.listar_restaurantes()

if __name__ == '__main__':
  main()