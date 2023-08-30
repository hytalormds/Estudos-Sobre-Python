# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo. #

from datetime import date
ano_nascimento = int(input('Entre com seu ano de nascimento: '))
sexo = str(input('Entre com o seu sexo: '))
cal = date.today() year - ano_nascimento
if sexo == 'feminino' or sexo == 'Feminino':
    print('Você não precisa se alistar')
elif cal < 18:
    print('Você não têm idade para se alistar nas forças armadas, você pode se alistar em {} anos: '.format(18 - cal))
elif cal == 18:
    print('Você deve se apresentar no próximo mês!')
else:
    print('Você já passou do tempo de alistamento em {} anos, se apresente para mais informações '.format(cal-18))