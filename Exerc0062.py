# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos. #

n1 = int(input('Entre com o 1° termo: '))
r = int(input('Entre com a razão: '))
i = total = 0
m = 10
while m != 0:
    total = total + m
    while i <= total:
        print('{} ->'.format(n1), end = '')
        n1 += r
        i += 1
        m = int(input('Quantos termos vc quer mostrar a mais?'))
print('Fim')        