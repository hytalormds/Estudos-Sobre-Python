# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores. #

op = 'S'
s = qtd = 0 
maior = menor = 0

while op == 'S':
    n = int(input('Entre com um número: '))
    op = str(input('Quer continuar ?[S/N]')).strip().upper()
    while op == 'S' and op == 'P':
        op = str(input('Quer continuar ?[S/N]')).strip().upper()
        s += n
        qtd += 1
        if qtd == 1:
            maior = menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
media = s / qtd
print('Média: {}'.format(media))
print('Maior: {}'.format(maior)) 
print('Menor: {}'.format(menor)) 
