# 7 - Crie um Arquivo Main (main.py): Crie um arquivo chamado main.py no mesmo diretório que suas classes.

# 8 - Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto. Em seguida, crie três instâncias de Carro e Moto com diferentes marcas, modelos, quantidade de portas e tipos.

from carro import Carro
from moto import Moto
# Instancie objetos
carro1 = Carro('Fiat', 'Uno', 4)
carro2 = Carro('Chevrolet', 'Onix', 4)
carro3 = Carro('Volkswagen', 'Gol', 4)
moto1 = Moto('Honda', 'CB 500', 'Casual')
moto2 = Moto('Yamaha', 'MT-07', 'Esportiva')
moto3 = Moto('Kawasaki', 'Ninja 400', 'Esportiva')

# 9 - Exiba as Informações: Para cada instância, imprima no console as informações utilizando o método str.

print(carro1)
print(carro2)
print(carro3)
print()
print(moto1)
print(moto2)
print(moto3)