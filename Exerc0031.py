# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas. #

km = float(input('Entre com os KM rodados: '))
if km <= 200:
    preço = km * 0.50
    print('A passagem no KM {} eh: {:.2f}R$'.format(km, preço))
else:
    preço = km * 0.45
    print('A passagem no KM {} eh: {:.2f}R$'.format(km, preço))
        