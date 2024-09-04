def linha(texto):
  linha = '=' * (len(texto))
  print(linha)

class Musica:
  nome = ''
  artista = ''
  duracao = int


lirica =  Musica()
lirica.nome = 'Lirica'
lirica.artista = 'Artista'
lirica.duracao = 355

lirica1 = Musica()
lirica1.nome = 'Lirica1'
lirica1.artista = 'Artista1'


lirica2 = Musica()
lirica2.nome = 'Lirica2'
lirica2.artista = 'Artista2'
lirica.duracao = 199

print(vars(lirica1))

class Musica:
    nome = ''
    artista = ''
    duracao = int

musica1 = Musica()
musica1.nome = 'Bohemian Rhapsody'
musica1.duracao = 355

print(f'Música: {musica1.nome} - Banda: {musica1.artista} - {musica1.duracao} segundos')


# Exercícios 

class Restaurante:
  nome = ''
  categoria = ''
  ativo = False


restaurante_da_praca = Restaurante()
restaurante_da_praca.nome = 'Pizza'

exercicio1 = '1 - Atribua o valor Italiana ao atributo categoria da instância restaurante_praca da classe Restaurante.'
linha(exercicio1)
print(exercicio1)
linha(exercicio1)
restaurante_da_praca.categoria = 'Italiana'
nome_do_restaurante = restaurante_da_praca.categoria
print(f'Resposta: {nome_do_restaurante}\n')

exercicio3 = '3 - Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo'
linha(exercicio3)
print(exercicio3)
linha(exercicio3)
if restaurante_da_praca.ativo:
   print('O restaurante está ativo\n')
else:
   print('O restaurante está inativo\n')

exercicio4 = '4 - Acesse o valor do atributo de classe categoria diretamente da classe Restaurante.'
linha(exercicio4)
print(exercicio4)
linha(exercicio4)
print(f'Resposta: {Restaurante.categoria}\n')

exercicio5 = '5 - Altere o valor do atributo nome para Bistrô.'
linha(exercicio5)
print(exercicio5)
linha(exercicio5)
restaurante_da_praca.nome = 'Bistrô'
print(f'Resposta: {restaurante_da_praca.nome}\n')

exercicio6 = '6 - Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome Pizza Place e categoria Fast Food.'
linha(exercicio6)
print(exercicio6)
linha(exercicio6)
restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
print(f'Resposta: {restaurante_pizza.nome} - {restaurante_pizza.categoria}\n')

exercicio7 = '7 - Verifique se a categoria da instância restaurante_pizza é Fast Food'
linha(exercicio7)
print(exercicio7)
linha(exercicio7)
if restaurante_pizza.categoria == 'Fast Food':
   print('A categoria é Fast Food\n')
else:
   print('A categoria não é Fast Food\n')

exercicio8 = '8 - Mude o estado da instância restaurante_pizza para ativo.'
linha(exercicio8)
print(exercicio8)
linha(exercicio8)
restaurante_pizza.ativo = True
print(f'Resposta: {restaurante_pizza.ativo}\n')

exercicio9 = '9 - Imprima no console o nome e a categoria da instância restaurante_praca.'
linha(exercicio9)
print(exercicio9)
linha(exercicio9)
print(f'Resposta: {restaurante_da_praca.nome} - {restaurante_da_praca.categoria}\n')