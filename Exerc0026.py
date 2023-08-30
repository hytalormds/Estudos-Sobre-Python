#  Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez. #

frase = str(input('Entre com o conteúdo: ')).upper().strip()
print('A frase poossui {}'.format(frase.count('A')))
print('A letra A aparece no início em {}'.format(frase.find('A')+1))
print('A letra A aparece no fim {}'.format(frase.rfind('A')+1))
