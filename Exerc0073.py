# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

#a) Os 5 primeiros times.

#b) Os últimos 4 colocados.

#c) Times em ordem alfabética.

#d) Em que posição está o time do Botafogo.

time = ('Palmeiras', 'Internacional', 'Fluminense', 'Flamengo', 'Corinthias', 'Athlético-PR', 'Atlético-MG', 'América-MG', 'Goiás', 'São Paulo', 'Botafogo', 'Santos', 'Bragantino', 'Fotaleza', 'Ceará-SC', 'Avaí', 'Cuiabá', 'Atlético-Go', 'Juventude')
for t in time:
    print(f'A ordem eh: {sorted(time)} = ''\n')
    print(f'Os 5 primeiros são: {time[0:5]}')
    print(f'Os 4 últimos são: {time[16:]}')
    print(f'O Botafogo se encontra em: {time.index("Botafogo")}lugar')
