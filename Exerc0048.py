# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500. #

s = 0
for i in range(1, 501):
    if i % 2 != 0:
        if i % 3 == 0:
            s += i
print('A soma dos números eh {}'.format(s))            