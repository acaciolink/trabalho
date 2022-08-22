
times = ( 'Palmeiras' ,'Corinthians', 'Fluminense', 'Athletico-PR',
          'Flamengo', 'Internacional', 'Atlético-MG', 'Bragantino',
          'Santos', 'São Paulo', 'Goiás', 'Botafogo', 'América-MG',
          'Ceará', 'Coritiba', 'Avaí', 'Cuiabá', 'Fortaleza', 'Atlético-GO','Juventude')
print('-='*20)
print('Lista de times:')
for t in times:
    print( f' {t}')
print('-='*20)
print(f'Os 5 primeiros times do brasileirao: {times[0:5]}')
print('-='*20)
print (f'Os 4 ultimos classificados são: {times[-4:]}')
print('-='*20)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-='*20)
g = input('Insira um time para saber a posição: ')
print( f'O time {g} esta na {times.index(g)+1}° posição')
print('-='*20)
