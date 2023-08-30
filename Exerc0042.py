# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: – EQUILÁTERO: todos os lados iguais – ISÓSCELES: dois lados iguais, um diferente – ESCALENO: todos os lados diferentes #

l1 = float(input('Entre com o lado 1: '))
l2 = float(input('Entre com o lado 2: '))
l3 = float(input('Entre com o lado 3: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l3:
    print('Os segmentos FORMAM um triângulo', end = ' ')
    if l1 == l2 == l3:
        print('Equlátero')
    if l1 != l2 != l3 != l1:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Os segmentos NÃO FORMAM um triângulo')                