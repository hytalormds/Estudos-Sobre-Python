#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.#

preço = float(input('Entre com o valor do produto: '))
nv_preço = preço - (preço * 5/100)
print('O novo preço é {}R$'.format(nv_preço))
