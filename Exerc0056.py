# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos. #

s = i = 0
v = 20000

for c in range(1, 5):
    nome = str(input('Entre com os nomes: '))
    idade = int(input('Entre com as idades: '))
    sexo = str(input('Entre com o seu sexo: '))
    s += idade
    if idade > v:
        v = idade
        n = nome
    if idade < 20 and sexo == 'f' or sexo == 'feminino' or sexo == 'Feminino':
        i += 1
media = s / 4
print('A média das idades eh: {}'.format(media))
print('A soma de mulheres menores que 20 anos eh: '.format(i))
print('O homem mais velho eh; {}'.format(nome))
            