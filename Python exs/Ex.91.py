#Playing Dices

from random import randint
from time import sleep
from operator import itemgetter

values = {'player1':randint(1,6),'player2':randint(1,6),'player3':randint(1,6),'player4':randint(1,6)}
ranking = {}

print('Sorted values: ')

for k,v in values.items():
    print(f'The {k} took {v} in dices.')
    sleep(0.5)

print('=-='*10)
print('PLAYERS RANKING'.center(30))

#sorted ranking

ranking = sorted(values.items(), key=itemgetter(1), reverse=True)

for i,v in enumerate(ranking):
    print(f'{i+1}º place: {v[0]}, with {v[1]}.')
print('=-='*10)