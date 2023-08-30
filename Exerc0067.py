# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. #

while True:
    n = int(input('Entre com os valores: '))
    if n < 0:
        break
    print('-'*30)
    for c in range(1, 11):
        print(f'{n} X {c:2} = {n*c}')
    print('-'*30)
print('Programa Encerrado')        