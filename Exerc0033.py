# Faça um programa que leia três números e mostre qual é o maior e qual é o menor. #

n1 = int(input('Entre com o primeiro número: '))
n2 = int(input('Entre com o segundo número: '))
n3 = int(input('Entre com o terceiro número: '))
menor = n1

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor valor eh: {}'.format(menor))
print('O maior valor eh: {}'.format(maior))           