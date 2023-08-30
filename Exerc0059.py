# Crie um programa que leia dois valores e mostre um menu na tela: [ 1 ] somar, [ 2 ] multiplicar, [ 3 ] maior, [ 4 ] novos números, [ 5 ] sair do programa. Seu programa deverá realizar a operação solicitada em cada caso. #

n1 = float(input('Entre com o 1° valor: '))
n2 = float(input('Entre com o 2° valor: '))
i = 0

while i != 5:
    print('\n[1] somar \n [2] multiplicar \n [3] maior \n [4] novos números \n [5] sair do programa')
    i = int(input('Escolha uma opção: '))
    if i == 1:
        print('A soma dos valores eh {}'.format(n1 + n2))
    elif i == 2:
        print('A soma dos valores eh {}'.format(n1 * n2))
    elif i == 3:
        if n1 > n2:
            print('N1 é maior que N2')
        else:
            print('N2 é maior que N1') 
    elif i == 4:
        n1 = float(input('Entre com o 1° valor: '))
        n2 = float(input('Entre com o 2° valor: '))  
    else:
        print('Número inválido. Digite Novamente')
print('FIM')                     
