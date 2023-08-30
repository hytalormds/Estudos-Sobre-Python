# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer. #

from random import randint
comp = randint(0, 10)
i = False
p = 0 
while not i:
    jog = int(input('Entre com um número: '))
    p += 1
    if jog == comp:
        i = True
    else:
        if jog < comp:
            print('Insira um número maior')
        elif jog > comp:
            print('Insira um número menor')
print('Acertou com {} tentativas !'.format(p))
                    