# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado. #

valor = float(input('Qual o valor da casa:R$'))
salário = float(input('Entre com o salário:R$'))
ano = int(input('Entre com os anos: '))
prestação = valor / (ano * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(valor, ano), end = ' ')
print('A prestação será de R$ {:.2f}'.format(prestação))
if prestação <= mínimo:
    print('\033[0; 32; 40 m Empréstimo CONCEDIDO!')
else:
    print('\033[0; 31; 40 m Empréstimo NÃO PODE SER CONCEDIDO!')
