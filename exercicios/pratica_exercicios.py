def linha():
  linha = '=' * 25
  print(linha)
linha()
# Questão 1
precos = {
  'celeular': 1500,
  'laptop': 2000,
  'tablet': 1000
}
for i in precos:
  print(f'{i}: {precos[i]}')

linha()
# Questão 2
numero = 1500
numero = f'R${numero:,.2f}'
print(numero)
linha()

# Questão 3
vendas = 4500
if vendas > 1000:
  print('Você bateu a primira meta')
elif vendas > 3000:
  print('Você bateu a segunda meta, bonus de R$200')
elif vendas > 4500:
  ('Você bateu a terceira meta, bonus de R$500')

if 1000 < vendas < 3000:
  print('Você bateu a primira meta')
elif 3000 <= vendas < 4500:
  print('Você bateu a segunda meta, bonus de R$200')
elif vendas >= 4500:
  print('Você bateu a terceira meta, bonus de R$500')

linha()
# Questão 4
lista = ['iphone', 'ipad', 'mac']
nova_lista = lista.append('airpod')
print(lista)
print(nova_lista)

# Questão 5
tax = 12.5 / 100
preco = 100.50
total = preco * tax
print(f'A taxa é {tax * 100}% e equivale a {round(total, 2)} de {preco}')

# Questão 6
print('C:\some\nome')
print(r'C:\some\nome')
print('Doesn\'t')
print("Doesn't")
print(3 * 'un' + 'in')
print('Py' 'thon')
prefix = 'Py'
print(prefix + 'thon')
# As strings são indexadas com indice partindo de 0 para cada caractere
# Index negativo numera os caracteres de trás para frente (iniciamdo em -1)
print('Python'[0])
print('Python'[1])
print('Python'[-3])
# A fatiação pode ser feita com [0:2] com o primeiro incluso e o último excluido
print('Python'[0:3])

# Podemos acessar itens em lista pelo índice como em strings
numeros = [1, 2, 3, 4, 5]
print(numeros[0])
print(numeros[-1])