# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla. #

from random import randint

num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),)

print(f'Os números gerados são: ')

for c in num:
    print(f'{num}')
    print(f'O maior número eh: {max(num)}')
    print(f'O menor número eh: {min(num)}')