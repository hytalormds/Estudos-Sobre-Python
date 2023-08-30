# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida: – Média abaixo de 5.0: REPROVADO – Média entre 5.0 e 6.9: RECUPERAÇÃO – Média 7.0 ou superior: APROVADO #

n1 = float(input('Entre com a primeira nota: '))
n2 = float(input('Entre com a segunda nota: '))
media = (n1 + n2) / 2
if media < 4.9:
    print('\033[1; 31; 40 m Reprovado')
elif media >= 5.0 and media <= 6.9:
    print('\033[1; 33; 40 m Recuperação')
else:
    print('\033[1; 32; 40 m Aprovado')
            