#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.#

real = float(input('Entre com o valor em real R$: '))
dolar = real / 5.16
print('Com R$ {:.2f} a pessoas pode comprar U$${:.2f}'.format(real, dolar))