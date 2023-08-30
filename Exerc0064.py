# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag). #

i = s = 0
c = -1

while i != 999:
    s += i
    i += i
    c += 1
    i = int(input('Digite um número [999 para parar]: '))
print('\n A soma dos valores eh: {} \n A quantidade de números digitados foi: {}'.format(s, c))    