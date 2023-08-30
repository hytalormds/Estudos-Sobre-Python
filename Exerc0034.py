# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%. #

sla = float(input('Entre com o salário:R$'))
novosla = sla + (sla * 10 / 100)
print('O novo salário superior  a 1250 eh: {:.2f} R$'.format(novosla))
if sla <= 1250:
    novosla = sla + (sla * 15/100)
    print('O novo salário inferior a 1250 eh: {:.2f}'.format(novosla))