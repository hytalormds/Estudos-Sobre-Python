# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome. #

nome = str(input('Entre com o nome :')).strip()
print('Seu nome têm Silva ? {}'.format('Silva' in nome.title()))
