# Faça um programa que leia um número qualquer e mostre o seu fatorial. #

n = int(input('Entre com um número: '))
f = 1
c = 1
while c <= n:
    f = f * c
    c += 1
print('O fatorial eh: {}'.format(f))
    