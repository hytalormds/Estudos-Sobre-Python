from random import choice

n1 = str(input('Entre com o primeiro nome: '))
n2 = str(input('Entre com o segundo nome: '))
n3 = str(input('Entre com o terceiro nome: '))
n4 = str(input('Entre com o quarto nome: '))

lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido eh: {}'.format(escolhido))