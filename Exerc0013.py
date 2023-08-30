# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.#

sl = float(input('Entre com o salário atual: '))
novo = sl + (sl * 15/100)
print('O novo salário eh {:.2f}'.format(novo))