class Restaurante:
  nome = ''
  categoria = ''
  ativo = False

restaurante_boizao = Restaurante()
restaurante_boizao.nome = 'Boizão'
restaurante_boizao.categoria = 'Churrascaria'

restaurante_forno = Restaurante()

restaurantes = [restaurante_boizao, restaurante_forno]

print(restaurante_boizao.ativo)