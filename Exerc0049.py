# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for. #

num = int(input('Entre com um número: '))
for i in range(1, 11):
    print('{} X {:2} = {}'.format(num, i, num * i))