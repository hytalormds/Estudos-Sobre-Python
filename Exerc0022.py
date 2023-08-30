# Crie um programa que leia o nome completo de uma pessoa e mostre: – O nome com todas as letras maiúsculas e minúsculas. – Quantas letras ao todo (sem considerar espaços). – Quantas letras tem o primeiro nome. #

nome = str(input('Entre com o nome completo: ')).strip()
print('O seu nome em maiúsculo é {}'.format(nome.upper()))
print('O seu nome em minúsculo é {}'.format(nome.lower()))
print('Seu nome ao todo têm {} letras'.format(len(nome)-nome.count(' ')))
#print('O seu primeiro nome têm {} letras'.format(nome.find('')))
sep = nome.split()
print('Seu primeiro nome é {} ele têm {} letras'.format(sep[0], len(sep[0])))
