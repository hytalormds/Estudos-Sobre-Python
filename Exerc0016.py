#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.#

from math import trunc

n = float(input('Digite um número com ponto flutuante: '))
print('O número real {} na sua forma inteira eh {}'.format(n , trunc(n)))