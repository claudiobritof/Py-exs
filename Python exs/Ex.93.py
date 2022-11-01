#Soccer player registration (in 3 ways of printing)

list = {}
goals = []

list['name'] = str(input('Player name: '))
matches = int(input(f'How many matches the player {list["name"]} has played? '))
if matches > 0:
    for c in range(0,matches):
        goals.append(int(input(f'How many goals in match {c}? ')))
        list['goals'] = goals[:]
        list['total'] = sum(goals)
else:
    print('The player hasnt played yet.')

print('=-='*20)
print(list)
print('=-='*20)

for k,v in list.items():
    print(f'{k} is equal to {v}.')

print('=-='*20)

print(f'The player {list["name"]} played {matches} matches.')

for i,v in enumerate(list['goals']):
    print(f'=> On the match {i}, he scored {v} goals.')

print(f'He scored a total of {list["total"]} goals.')