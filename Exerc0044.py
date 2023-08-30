# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: – à vista dinheiro/cheque: 10% de desconto – à vista no cartão: 5% de desconto – em até 2x no cartão: preço formal  – 3x ou mais no cartão: 20% de juros #

valor = float(input('Entre com o valor do pagamento do produto:R$'))
pesq = int(input('Escolha a forma de pagamento :\n 1 - À vista no dinheiro/cheque; \n 2 - À vista no cartão; \n 3 - 2X no cartão; \n 4 - 3X no cartão; '))

if pesq == 1:
    print('O valor a ser pago será {:.2f} R$'.format(valor - (valor * 0.1)))
elif pesq == 2:
    print('O valor a ser pago será {:.2f} R$'.format(valor - (valor * 0.05)))
elif pesq == 3:
    print('O valor a ser pago será {:.2f} R$'.format(valor))
elif pesq == 4:
    print('O valor a ser pago será {:.2f} R$'.format(valor * 0.2))
else:
    print('Não há uma forma de pagamento !')                