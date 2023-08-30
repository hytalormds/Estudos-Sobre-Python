# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu. #

from random import radint
comp = radint(0, 5)
print('-=-'*20)
print('Irei pensar em um número entre 0 e 5 ....')
print('-=-'*20)
jog = int(input('Entre com um número: '))
if comp == jog:
    print('Parabéns você acertou o número !')
else:
    print('Que pena eu pensei em {} você em {}, tente novamente'.format(comp, jog))
