# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite. #

km = float(input('Entre com a velocidade do carro em KM: '))
if km > 80:
    print('Você foi multado')
    m = (km - 80) * 7
    print('Você vai pagar R$ de multa'.format(m))
else:
    print('Você está no limite normal') 
