# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre: A) qual é o total gasto na compra. B) quantos produtos custam mais de R$1000. C) qual é o nome do produto mais barato. #

tot = qtd = menor = cont = 0
barato = ' '
while True:
    nome = str(input('Entre com o nome do produto: '))
    preço = float(input('Entre com o preço: '))
    cont += 1
    tot += preço
    if preço > 1000:
        qtd += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar ?[S/N]: ')).strip().upper()[0]
        if res == 'N':
            break
print(f'O tatal da compra eh: {tot :.2f}')
print(f'A quantidade de produtos que custam mais que 1000 eh: {qtd}') 
print(f'O produto mais barato eh: {barato}')
           