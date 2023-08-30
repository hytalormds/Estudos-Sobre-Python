#  Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. #

from random import randint

v = 0 
print('VAMOS JOGAR ÍMPAR OU PAR')

while True:
    n = int(input('Entre com os valores: '))
    c = randint (0, 10)
    total = n + c
    tipo = ''
    while tipo in 'PI':
        tipo = str(input('Ímpar ou Par?')).strip().upper()[0]
        print(f'Você jogou {n} e o computador {c}. Total de {total}')
        if tipo == 'P':
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
print(f'Você ganhou {v} vezes')            
