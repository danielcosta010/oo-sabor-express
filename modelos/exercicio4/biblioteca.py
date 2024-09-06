# 5 - Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

from atividade_aula4 import Livro

# 6 - No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.

livro_1 = Livro('Biblia', 'Deus', 0)
livro_2 = Livro('Genesis', 'Deus/Moises', 0)
livro_3 = Livro('Prometeus', 'tetrarca', 1895)
livro_4 = Livro('Pitolomeu', 'duodarca', 1995)
livro_5 = Livro('Denarios', 'Triarca', 1895)
livro_2.emprestar()
livro_4.emprestar()

# 7 - No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.

print(Livro.verificar_disponibilidade(0))
print(livro_1)
print(livro_2)
print(livro_3)
print(livro_4)
print(livro_5)