# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. #

from datetime import date
atual = date.today().year
ma = 0
me = 0
for c in range(1, 8):
    ano = int(input('Entre com o ano de nascimento: '))
    cal = atual - ano
    if cal >= 18:
        ma += 1
    elif cal < 18:
        me += 1
print('A quantidade de pessoas maiores de idade eh: {}'.format(ma))
print('A quantidade de pessoas menores de idade eh: {}'.format(me))            