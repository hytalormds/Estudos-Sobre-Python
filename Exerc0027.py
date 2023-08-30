# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. #

n = str(input('Entre com o nome: ')).strip()
nome = n.split()
print('O nome completo eh: {}'.format(n))
print('O primeiro nomr eh: {}'.format(nome[0]))
print('O último nome eh: {}'.format(nome[len(nome)-1]))
