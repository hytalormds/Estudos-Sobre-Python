# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. #

n = int(input('Entre com o valor: '))
t = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[32 m', end = ' ')
        t += 1
if t == 2:
    print('O número {} é primo'.format(n), end = '') 
else:
    print('O número {} não é primo'.format(n), end = '')           
