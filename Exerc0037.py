# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal. #

n = int(input('Entre com o número: '))
pesq = int(input('Entre com um número de pesquisa 1 - Binário, 2 - Octal, 3 - Hexadecimal: '))

if pesq == 1:
    print('O número {} convertido em Binário eh: {}'.format(n, bin(n)))
elif pesq == 2:
    print('O número {} convertido em Octal eh: {}'.format(n, oct(n)))
elif pesq == 3:
    print('O número {} convertido em Hexadecimal eh: {}'.format(n, hex(n)))   
else:
    print('\033[0; 31; 40 m Número não encontrado!')    