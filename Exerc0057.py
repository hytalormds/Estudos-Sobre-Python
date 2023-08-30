# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto. #

s = str(input('Entre com o sexo: ')).strip().upper()[0]
while s not in 'MmFf':
    s = str(input('Dados inválidos. Insira o seu sexo novamente: ')).strip().upper()[0]
print('Sexo{} registrado com sucesso'.format(s))
    