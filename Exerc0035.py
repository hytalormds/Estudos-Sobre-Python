# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo. #

l1 = float(input('Entre com o lado 1: '))
l2 = float(input('Entre com o lado 2: '))
l3 = float (input('Entre com o lado 3: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l3:
    print('Os segmentos FORMAM um triângulo')
else:
    print('Os segmentos NÃO FORMAM um triângulo') 
    
       