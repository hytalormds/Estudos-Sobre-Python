#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.#

from math import hypot

ca = float(input('Entre com o cateto adjacente: '))
co = float(input('Entre com o cateto oposto: '))
h = hypot(co, ca)
print('A hipotenusa vai mediar {:.2f}'.format(h))
