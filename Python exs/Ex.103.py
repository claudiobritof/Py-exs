#How many goals a player scored on a tournament?

def ficha(name='<desconhecido>',goals=0):
    print(f'The player {name} scored {goals} goal(s) on the tournament.')


n = str(input('Player name: ')).capitalize().strip()
g = str(input(f'How many goals {n} scored? '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    ficha(goals=g)
else:
    ficha(n,g)