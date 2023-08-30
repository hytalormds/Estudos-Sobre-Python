# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o. #

s = 0
for i in range(1, 7):
    n = int(input('Entre com os valores: '))
    if n % 2 == 0:
        s += i
print('A soma dos valores eh: {}'.format(s)) 
       