from math import radians, cos, sin, tan

ang = int(input('Entre com o ângulo: '))
cosseno = cos(radians(ang))
seno = sin(radians(ang))
tangente = tan(radians(ang))

print('O COSSENO do ângulo {} é {:.2f}'.format(ang, cosseno))
print('O SENO do ângulo {} é {:.2f}'.format(ang, seno))
print('A TANGENTE do ângulo {} é {:.2f}'.format(ang, tangente))
