#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.#

c = float(input('Entre com a temperatura em graus °C: '))
f = (c * 1.8) + 32
print('O valor {:.1f} °C convertido para {:.1f} °F'.format(c, f))