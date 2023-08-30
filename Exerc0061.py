# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while. #

n1 = int(input('Entre com o 1° termo: '))
r = int(input('Entre com a razão: '))
i = 1
while i <= 10:
    n1 += r
    i += 1
    print('{}'.format(n1), end = ' ')
print('Fim')        