# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: A) quantas pessoas tem mais de 18 anos. B) quantos homens foram cadastrados. C) quantas mulheres tem menos de 20 anos. #

qtd = mas = fem = 0

while True:
    idade = int(input('Entre com as idades: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Entre com o sexo: ')).strip().upper()[0]
        if idade >= 18:
            qtd += 1
        if sexo == 'M':
            mas += 1
        if sexo == 'F' and idade < 20:
            fem += 1
        resp = ' '
        while resp not in'SN':
            resp = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
            if resp == 'N':
                break
print(f'A quantidade de pessoas maiores de 18 eh: {qtd}')
print(f'A quantidade de homens eh: {mas}')
print(f'A quantidade de mulheres menores de 20 anos eh: {fem}')                        

