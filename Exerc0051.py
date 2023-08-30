# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão. #

n1 = int(input('Primeiro termo: '))
r = int(input('Razão: ')) 
n10 = n1 + (10 - 1) * r
for i in range(n1, n10 + r, r):
    print('{}'.format(i), end = '\n')