#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.#

m = float(input('Entre com a média em metros: '))
c = m * 100
mi = m * 1000
print('O valor convertido de metros para centímetros {:.0f} \n O valor convertido de metros para milímetros {:.0f}'. format(c, mi))