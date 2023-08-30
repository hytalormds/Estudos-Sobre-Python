# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos. #

maior = 0
menor = 9999999

for c in range(1, 6):
    peso = float(input('Entre com o peso: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior eh: {}'.format(maior))
print('O menor eh: {}'.format(menor))         