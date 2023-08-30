# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”. #

c = str(input('Entre com o nome da cidade: ')).strip()
print(c[:5].upper()=='Santo')
