#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.#

l = float(input('Entre com a largura: '))
al = float(input('Entre com a altura: '))
a = l * al
tinta = a / 2

print('A área da parede e {} x {} = {} m^2 \n A  quantidade de tinta necessária é {}L'.format(l, al, a, tinta))
